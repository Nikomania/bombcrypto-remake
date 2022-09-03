from ursina import *
from ursina.trigger import Trigger

from threading import Timer


class Bombs:
    def __init__(self):
        self.bombs = dict()
        # Explosion textures
        self.explosion_level = ("1_00", "2_00", "2_01", "3_00", "3_01", "3_02", "3_03")
        self.explosion_objects = dict()

    def collision(self, bomb):
        self.bombs[bomb][1].collider = "box"

    def create_fire(self, bomb, pos, level):
        self.explosion_objects[bomb].append(Entity(model="quad",
                                                   texture=f"materials/sprite/fire{self.explosion_level[level]}.png",
                                                   always_on_top=True,
                                                   scale=(1, 1),
                                                   render_queue=0,
                                                   eternal=False,
                                                   position=pos))

    def delete_objects(self, *pos):
        [destroy(i) for i in self.explosion_objects[pos]]
        self.explosion_objects.pop(pos)

    def explode(self, *bomb, rng=2):
        [destroy(i) for i in self.bombs[bomb]]
        self.bombs.pop(bomb)

        # Bomb pos
        x, y = bomb
        self.explosion_objects[bomb] = list()
        # Explosion central point
        self.create_fire(bomb, (x, y), 0)
        # Explosion body
        for i in range(1, rng):
            for t in (((x+i, y), 1), ((x-i, y), 1), ((x, y+i), 2), ((x, y-i), 2)):
                self.create_fire(bomb, *t)
        # Explosion edge
        for i in (((x+rng, y), 3), ((x, y+rng), 4), ((x-rng, y), 5), ((x, y-rng), 6)):
            self.create_fire(bomb, *i)

        Timer(.8, self.delete_objects, args=bomb).start()

    def plant(self, p, explosion_time=5):
        # Player position
        pos = p.get_player_position()

        # Check if bomb already exists
        if pos not in self.bombs.keys():
            # [Trigger, model]
            self.bombs[pos] = [Trigger(model="sphere",
                                       trigger_targets=(p.get_jogador(),),
                                       position=pos,
                                       color=color.clear,
                                       radius=.5),
                               Entity(model="quad",
                                      texture="materials/models/bomb0.png",
                                      always_on_top=True,
                                      scale=(.6, .6),
                                      render_queue=0,
                                      eternal=False,
                                      position=pos)]

            # Triggers
            # Set bomb collision after player jumps out
            self.bombs[pos][0].on_trigger_exit = Func(self.collision, pos)

            # Explode the bomb in X seconds (explosion_time)
            # Will use another thread (threading)
            Timer(explosion_time, self.explode, args=pos).start()
