from ursina import Entity
from ursina import *

from src.healthbar import Health


class Personagem(object):
    def __init__(self, player_pos, last_key=''):
        self.jogador = Entity(model="quad",
                              texture="materials/player/player_1.png",
                              always_on_top=True,
                              scale=(.6, .7),
                              render_queue=1,
                              eternal=False,
                              collider="box",
                              # Just a start space to prevent bugs (wall collision)
                              position=(player_pos[0], player_pos[1], 0))

        self.ghost = Entity(model="quad",
                            color=color.clear,
                            always_on_top=False,
                            scale=(.6, .7),
                            render_queue=1,
                            eternal=False,
                            collider="box",
                            # Just a start space to prevent bugs (wall collision)
                            position=(player_pos[0], player_pos[1], 0))

        self.last_key = last_key
        self.x = self.jogador.x
        self.y = self.jogador.y

        self.health = Health(self.jogador)

    def get_jogador(self):
        return self.jogador

    def get_player_position(self):
        return round(self.jogador.x, 0), round(self.jogador.y, 0)

    def walk(self, movimento, x, y):
        p, g = self.jogador, self.ghost
        p.texture = movimento + ".png"
        
        # self.jogador.texture = Animation("resources/player/player", autoplay=True, loop=True)

        # Collision method
        g.x += x
        g.y += y
    
        hit_info = g.intersects(ignore=(p,))
        if not hit_info.hit:
            p.x += x
            p.y += y

        g.position = p.position
            # destroy(hit_info.entity)
        # Prevent the player get stucked into the block
        self.last_key = movimento

    def get_last_key(self):
        return self.last_key
