# Engine
from ursina import *

# Source
from src.personagem import Personagem
from src.mapas import Mapa
from src.bomb import Bombs


if __name__ == "__main__":
    DEVELOPMENT_MODE = True

    game = Ursina(title="BombCrypto Remake",
                  vsync=True,
                  fullscreen=False,
                  borderless=False,
                  forced_aspect_ratio=True,
                  show_ursina_splash=not DEVELOPMENT_MODE,
                  development_mode=DEVELOPMENT_MODE,
                  editor_ui_enabled=DEVELOPMENT_MODE)

    # application.compressed_textures_folder = application.compressed_textures_folder.parent / "resources"
    # application.asset_folder = application.compressed_textures_folder
    # application.internal_textures_folder = application.compressed_textures_folder

    PLAYER_SPEED = 0.07
    PLAYER_POS = (4, 4)

    JOGADOR = Personagem(PLAYER_POS)
    BOMBA = Bombs()

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

    # Key: button pressed
    # First value of tuple: Function
    # Second value of tuple: Parameters
    COMANDOS = {'w': (JOGADOR.walk, ["player/player_costas", 0, PLAYER_SPEED]),
                'a': (JOGADOR.walk, ["player/player_esq", -PLAYER_SPEED, 0]),
                's': (JOGADOR.walk, ["player/player_1", 0, -PLAYER_SPEED]),
                'd': (JOGADOR.walk, ["player/player_dir", PLAYER_SPEED, 0]),
                "space": (BOMBA.plant, [JOGADOR]),
                '1': (BOMBA.explode, [])}

    
    def update():
        global COMANDOS
        for key, value in held_keys.items():
            if key in COMANDOS and value != 0:
                # Take all the params
                params = COMANDOS[key][1]
                # Take the first param as function variable to the next test
                func = params[0] if len(params) > 0 else False
                # If the params it's a function, this statement will execute it to return the real params
                # Else, it will just execute normally with params that're given before
                COMANDOS[key][0](func()) if callable(func) else COMANDOS[key][0](*params)

    MAPA.gerar_mapa()
    camera.add_script(SmoothFollow(target=JOGADOR.get_jogador(), offset=(0, 0, -20), speed=10))
    game.run()
