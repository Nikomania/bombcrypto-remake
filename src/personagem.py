from ursina import Entity
from ursina import *

from src.healthbar import Health

# Todo: Code refactoring !!!


class Personagem():
    def __init__(self, player_pos, last_key=''):
        self.jogador = Entity(model="quad",
                              texture="materials/player/player_1.png",
                              always_on_top=True,
                              scale=(.6, .7),
                              render_queue=10,
                              eternal=False,
                              collider="box",
                              # Just a start space to prevent bugs (wall collision)
                              position=(player_pos[0], player_pos[1], 0))
        self.last_key = last_key
        self.x = self.jogador.x
        self.y = self.jogador.y

        self.hp = Health(self.jogador)

    def get_jogador(self):
        return self.jogador

    def get_player_position(self):
        return round(self.jogador.x, 0), round(self.jogador.y, 0)

    def walk(self, movimento, x, y):
        self.jogador.texture = movimento + ".png"
        # self.jogador.texture = Animation("resources/player/player", autoplay=True, loop=True)

        # Collision method
        p = self.jogador
        hit_info = p.intersects()
        pos = hit_info.world_point
        if not hit_info.hit:
            p.x += x
            p.y += y

            # destroy(hit_info.entity)
        # Prevent the player get stucked into the block
        else:
            # Todo: Do the corner checks (bug)
            if not p.x + x >= pos[0] and x < 0 or\
                    not p.x + x <= pos[0] and x > 0:
                p.x += x
            elif not p.y + y >= pos[1] and y < 0 or\
                    not p.y + y <= pos[1] and y > 0:
                p.y += y

        self.last_key = movimento

    def get_last_key(self):
        return self.last_key

    # Todo: Refactor this to the right way
    def hit(self, damage):
        self.hp.hit(damage)
