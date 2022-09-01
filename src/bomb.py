from ursina import Entity
from ursina import *
from ursina.trigger import Trigger

from src.personagem import Personagem


class Bomb:
    def __init__(self, bombs=None):
        bombs = [] if bombs is None else None
        self.bombs = bombs

    def collision(self):
        self.bombs[-1][1].collider = "box"

    def plant(self, p):
        # Player position
        pos = p.get_player_position()

        # Check if bomb already exists
        if pos not in [(x[1].x, x[1].y) for x in self.bombs]:
            # [Trigger, model]
            self.bombs.append([Trigger(model="sphere",
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
                                      position=pos)])

            # Triggers
            # Set bomb collision after player jumps out
            self.bombs[-1][0].on_trigger_exit = Func(self.collision)

    def explode(self):
        if len(self.bombs) > 0:
            [destroy(i) for i in self.bombs[0]]
            self.bombs.pop(0)
