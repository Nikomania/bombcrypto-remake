from ursina import *

# Todo: Tilemap editor


class MapGenerator(object):
    def __init__(self, map_textures):
        self.map_textures = map_textures
        self.colliders = ("map/brick", "map/something")
        self.map = {}

    def generate(self):
        # Map generation (x, y)
        # Doesn't need to be square
        for x in range(len(self.map_textures)):
            for y in range(len(self.map_textures[x])):
                e = Entity(model="quad",
                           texture=self.map_textures[x][y] + ".png",
                           visible=True,
                           render_queue=0,
                           x=x,
                           y=y,
                           eternal=False)
                # Put into a vector list to future things
                self.map[(e.x, e.y)] = e

                # Objects with collision
                if self.map_textures[x][y] in self.colliders:
                    e.collider = "box"

    @property
    def map_objects(self):
        return self.map
