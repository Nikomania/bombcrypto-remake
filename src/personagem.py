from ursina import Entity
# Problema no import, precisamos achar o time.dt
from ursina import *


class Personagem(object):
    def __init__(self, last_key=''):
        self.jogador = Entity(model="quad",
                              texture="materials/player/player_1.png",
                              always_on_top=True,
                              scale=(.6, .7),
                              render_queue=1,
                              eternal=False,
                              collider="box")
        # Just a start space to prevent bugs (wall collision)
        self.jogador.x, self.jogador.y = 2, 2
        self.last_key = last_key

    def get_jogador(self):
        return self.jogador

    def get_world_position(self):
        return self.jogador.world_position

    def walk(self, movimento, x, y):
        # teste = self.jogador.x + x * time.dt * 100

        self.jogador.texture = movimento + ".png"
        # self.jogador.texture = Animation("resources/player/player", autoplay=True, loop=True)

        # Collision method
        hit_info = self.jogador.intersects()
        if not hit_info.hit:
            self.jogador.x += x
            self.jogador.y += y

            # destroy(hit_info.entity)
        # Prevent the player get stucked into the block
        else:
            # To-do: Do the corner checks (bug)
            if not self.jogador.x + x >= hit_info.world_point[0] and x < 0 or\
                    not self.jogador.x + x <= hit_info.world_point[0] and x > 0:
                self.jogador.x += x
            elif not self.jogador.y + y >= hit_info.world_point[1] and y < 0 or\
                    not self.jogador.y + y <= hit_info.world_point[1] and y > 0:
                self.jogador.y += y

        self.last_key = movimento

    def get_last_key(self):
        return self.last_key


