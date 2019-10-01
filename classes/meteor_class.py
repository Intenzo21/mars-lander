"""
Contains class for the meteor sprite.
"""

from .sprite_class import *
from random import uniform


class Meteor(Sprite):
    """
    METEOR SPRITE SUBCLASS
    """

    def __init__(self, image_file, top, left):
        super().__init__(image_file, top, left)
        self.veloc_y = uniform(5, 10)  # Meteor vertical speed
        self.veloc_x = uniform(-2, 2)  # Meteor horizontal speed

    def update(self):
        """
        Update meteor speed
        """

        self.rect.x += self.veloc_x
        self.rect.y += self.veloc_y
