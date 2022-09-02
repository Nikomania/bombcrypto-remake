from ursina import Entity
from ursina import *
from ursina.trigger import Trigger

from src.personagem import Personagem

from threading import Timer


class Bombs:
    def __init__(self, bombs=None):
        bombs = dict() if bombs is None else None
        self.bombs = bombs

    def collision(self, bomb):
        self.bombs[bomb][1].collider = "box"

    def explode(self, *bomb):
        [destroy(i) for i in self.bombs[bomb]]
        self.bombs.pop(bomb)

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
