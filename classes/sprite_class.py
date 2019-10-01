"""
Contains sprite superclass.
"""
import pygame


class Sprite(pygame.sprite.Sprite):
    """
    SPRITE SUPERCLASS
    """

    def __init__(self, image_file, top, left):
        super().__init__()
        self.image = pygame.image.load(image_file)  # Load image file
        self.rect = self.image.get_rect()  # Get the rectangular area of the Surface
        self.rect.top = top  # Position of the top side of the Sprite
        self.rect.left = left  # Position of the left side of the Sprite
