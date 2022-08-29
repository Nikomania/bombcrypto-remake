# Engine
from ursina import *
from ursina import application

# Source
from src.personagem import Personagem
from src.mapas import Mapa
from src.bomb import Bomb


if __name__ == "__main__":
    jogo = Ursina(vsync=True,
                  fullscreen=False)
    # print(application.compressed_textures_folder)
    # application.compressed_textures_folder = application.compressed_textures_folder.parent / "resources"
    # application.asset_folder = application.compressed_textures_folder
    # application.internal_textures_folder = application.compressed_textures_folder
    # print(application.compressed_textures_folder)
    JOGADOR = Personagem()
    BOMBA = Bomb()
    PLAYER_SPEED = 0.07
    PLAYER_POS = (0, 0)

    MAPA1 = [["map/brick", "map/brick", "map/brick", "map/brick", "map/brick", "map/brick", "map/brick", "map/brick", "map/brick"],
             ["map/brick", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/brick"],
             ["map/brick", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/brick"],
             ["map/brick", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/brick"],
             ["map/brick", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/brick"],
             ["map/brick", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/brick"],
             ["map/brick", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/brick"],
             ["map/brick", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/brick"],
             ["map/brick", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/fundo", "map/brick"],
             ["map/brick", "map/brick", "map/brick", "map/brick", "map/brick", "map/brick", "map/brick", "map/brick", "map/brick"]]

    MAPA = Mapa(MAPA1)

    COMANDOS = {'w': JOGADOR.walk,
                'a': JOGADOR.walk,
                's': JOGADOR.walk,
                'd': JOGADOR.walk,
                "space": BOMBA.plant,
                '1': BOMBA.explode}

    PARAMETROS = [["player/player_costas", 0, PLAYER_SPEED],   # W
                  ["player/player_esq", -PLAYER_SPEED, 0],     # A
                  ["player/player_1", 0, -PLAYER_SPEED],       # S
                  ["player/player_dir", PLAYER_SPEED, 0],      # D
                  [JOGADOR.get_player_position],               # SPACE
                  []]                                          # 1 - TEST


    def update():
        global COMANDOS, PARAMETROS, PLAYER_POS
        PLAYER_POS = JOGADOR.get_player_position()
        for key, value in held_keys.items():
            if key in COMANDOS.keys() and value != 0:
                # Take all the params
                params = PARAMETROS[list(COMANDOS.keys()).index(key)]
                # Take the first param as function variable to the next test
                func = params[0] if len(params) > 0 else False
                # If the params it's a function, this statement will execute it to return the real params
                # Else, it will just execute normally with params that're given before
                COMANDOS[key](func()) if callable(func) else COMANDOS[key](*params)

    MAPA.gerar_mapa()
    camera.add_script(SmoothFollow(target=JOGADOR.get_jogador(), offset=(0, 0, -50), speed=6))
    jogo.run()
