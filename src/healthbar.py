from ursina import *


class Health:
    def __init__(self, parent, max_hp=100, health=100):
        # HP Bar will follow the parent
        self.parent = parent
        self.max_hp = max_hp
        self.health = health

        # Constructor
        # Todo: Bar position bug
        self.model = [  # HP Bar
                        Entity(model="quad",
                               parent=self.parent,
                               # A small rect
                               scale=(1*health/100, .1),
                               render_queue=5,
                               always_on_top=True,
                               # Small fixes to scale
                               x=self.parent.x * -.01,
                               y=self.parent.y * .18,
                               color=color.green),
                        # HP Background (Visual)
                        Entity(model="quad",
                               parent=self.parent,
                               # A small rect
                               scale=(1.12, .2),
                               render_queue=4,
                               always_on_top=True,
                               # Small fixes to scale
                               x=self.parent.x * -.008,
                               y=self.parent.y * .18,
                               color=rgb(55, 34, 34))
                    ]

        # Easier to call
        self.bar = self.model[0]

    @property
    def hp(self):
        return self.health

    @hp.setter
    def hp(self, new_hp):
        self.health = new_hp

    def hit(self, damage):
        self.health -= damage
        self.bar.scale = (1*self.health/100, .1)
        print(self.health)  # Debug

    # Just delete all the elements
    def kill(self):
        [destroy(x) for x in self.model]
