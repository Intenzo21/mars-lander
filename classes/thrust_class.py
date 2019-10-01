"""
Contains class for the engine thrust sprite.
"""

from .sprite_class import *


class EngineThrust(Sprite):
    """
    THRUST SPRITE SUBCLASS
    """

    def __init__(self, lander_rect, lander_angle):
        super().__init__('images/thrust.png', lander_rect.bottom - 10, lander_rect.left + 31)
        self.rot_image = pygame.transform.rotate(self.image, lander_angle)
