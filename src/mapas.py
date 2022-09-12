from ursina import *

# Todo: Code refactoring
# Todo: Tilemap editor


class Mapa(object):
    def __init__(self, texturas):
        self.texturas = texturas
        self.map = {}

    def gerar_mapa(self):
        # Map generation (x, y)
        # Doesn't need to be square
        for x in range(len(self.texturas)):
            for y in range(len(self.texturas[x])):
                e = Entity(model="quad",
                           texture=self.texturas[x][y] + ".png",
                           visible=True,
                           render_queue=0,
                           x=x,
                           y=y,
                           eternal=False)
                # Put into a vector list to future things
                self.map[(e.x, e.y)] = e

                # Objects with collision
                if self.texturas[x][y] in ("map/brick", "map/something"):
                    e.collider = "box"

        # To-do: Each block converted into object blocks (future interaction)

    @property
    def map_objects(self):
        return self.map
