# Engine do jogo
from ursina import *
from ursina import application

# Importar as classes
from src.personagem import Personagem
from src.mapas import Mapa


if __name__ == "__main__":
    jogo = Ursina(vsync=True,
                  fullscreen=False)
    # print(application.compressed_textures_folder)
    # application.compressed_textures_folder = application.compressed_textures_folder.parent / "resources"
    # application.asset_folder = application.compressed_textures_folder
    # application.internal_textures_folder = application.compressed_textures_folder
    # print(application.compressed_textures_folder)
    JOGADOR = Personagem()

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

    COMANDOS = {'w': JOGADOR.andar,
                'a': JOGADOR.andar,
                's': JOGADOR.andar,
                'd': JOGADOR.andar,
                "space": scene.clear,
                '1': MAPA.gerar_mapa,
                '2': MAPA.gerar_mapa}

    PARAMETROS = (["player/player_costas", 0, 0.05],   # W
                  ["player/player_esq", -0.05, 0],     # A
                  ["player/player_1", 0, -0.05],         # S
                  ["player/player_dir", 0.05, 0],      # D
                  [],                           # SPACE
                  [],                           # 1
                  ["map/brick"])                    # 2


    def update():
        global COMANDOS, PARAMETROS
        for key, value in held_keys.items():
            if key in COMANDOS.keys() and value != 0:
                COMANDOS[key](*PARAMETROS[list(COMANDOS.keys()).index(key)])


    MAPA.gerar_mapa()
    camera.add_script(SmoothFollow(target=JOGADOR.get_jogador(), offset=(0, 0, -40), speed=5))
    jogo.run()
