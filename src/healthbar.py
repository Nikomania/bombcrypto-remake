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
                               scale=(health/100, .1),
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
    def hp(self, n):
        # Check if HP > 0 and HP < max_hp
        if self.max_hp > self.health + n > 0:
            self.health = self.health + n
        # Entity can't get more than the max_hp
        elif self.health + n >= self.max_hp:
            self.health = self.max_hp
        # Entity dies without negative hp
        elif self.health + n < 0:
            # Todo: Entity dies
            self.health = -1
        # Update HP bar
        self.bar.scale = (self.health / 100, .1)

    # Just delete all the elements
    def kill(self):
        [destroy(x) for x in self.model]
