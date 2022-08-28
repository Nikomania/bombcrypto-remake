from ursina import Entity
# Problema no import, precisamos achar o time.dt
from ursina import *


class Personagem(object):
    time.dt = 0

    def __init__(self, last_key=''):
        self.jogador = Entity(model="quad",
                              texture="materials/player/player_1.png",
                              always_on_top=True,
                              scale=(.6, .7),
                              render_queue=1,
                              eternal=False)
        self.last_key = last_key

    def get_jogador(self):
        return self.jogador

    def andar(self, movimento, x, y):
        self.jogador.texture = movimento + ".png"
        # self.jogador.texture = Animation("resources/player/player", autoplay=True, loop=True)
        self.jogador.x += x * time.dt * 100
        self.jogador.y += y * time.dt * 100
        self.last_key = movimento

    def get_last_key(self):
        return self.last_key


