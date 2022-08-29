from ursina import Entity
from ursina import *

from src.personagem import Personagem


class Bomb:
    def __init__(self, bombs=None):
        bombs = [] if bombs is None else None
        self.bombs = bombs

    def plant(self, pos):
        self.bombs.append(Entity(model="quad",
                                 texture="materials/models/bomb0.png",
                                 always_on_top=True,
                                 scale=(.6, .6),
                                 render_queue=0,
                                 eternal=False,
                                 collider="box",
                                 position=(pos[0], pos[1], 0)))

    def explode(self):
        if len(self.bombs) > 0:
            destroy(self.bombs[0])
            self.bombs.pop(0)
