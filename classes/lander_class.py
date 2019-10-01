"""
Contains class for the engine lander sprite with all functionalities.
"""

from .thrust_class import *
import math  # Used to calculate the magnitude of the gravity force applied on the lander
from random import uniform, randint


class Lander(Sprite):
    """
    LANDER SPRITE SUBCLASS
    """

    def __init__(self, width):
        super().__init__('images/lander.png', 0, 0)
        self.width = width
        self.veloc_y = uniform(0.0, 1.0)  # Set initial y-axis velocity to random float number between 0 and 1
        self.veloc_x = uniform(-1.0, 1.0)  # Set initial x-axis velocity to random float number between -1 and 1
        self.fuel = 500  # Set starting fuel to 500
        self.angle = 0  # Set initial angle to 0
        self.damage = 0  # Lander damage initially set to 0
        self.rot_image = self.image  # Holds rotated sprite
        self.reset_stats()

    def reset_stats(self):
        """Reset lander stats"""

        self.rect.top = 0
        self.rect.left = randint(0, self.width - self.rect.width)
        self.veloc_y = uniform(0.0, 1.0)
        self.veloc_x = uniform(-1.0, 1.0)
        self.fuel = 500
        self.angle = 0
        self.damage = 0
        self.rot_image = self.image

    def free_fall(self):
        """Check if the lander has left any of the borders and update lander y and x-axis speed"""

        if self.rect.top < 0:
            self.rect.top = 0
            self.veloc_y = uniform(0.0, 1.0)

        if self.rect.right < 0:
            self.rect.left = self.width

        if self.rect.left > self.width:
            self.rect.right = 0

        self.rect.y += self.veloc_y
        self.rect.x += self.veloc_x
        self.veloc_y += 0.1  # Gradually increment y-axis speed (gravity effect)

    def start_engine(self):
        """Calculate by how much the x and y-axis speed should be incremented considering the rotation angle
        and decrement fuel by 5"""

        self.veloc_x = self.veloc_x + 0.33 * math.sin(math.radians(-self.angle))
        self.veloc_y = self.veloc_y - 0.33 * math.cos(math.radians(self.angle))
        self.fuel -= 5

    @property
    def altitude(self):
        """Return distance from lander to Martian surface"""

        return 1000 - self.rect.top * 1.436

    @property
    def can_land(self):
        """Check if the lander has run out of fuel and if the damage it has sustained is below 100%"""

        return self.fuel > 0 and self.damage < 100

    def has_landing_position(self):
        """Check if the lander has landed correctly on the landing pad (proper y and x-axis
        velocity, landing angle, the lander's sustained damage must be lower than 100%) """

        return self.can_land and (self.veloc_y < 5) and (-5 < self.veloc_x < 5) and (-7 <= self.angle <= 7)

    def handle_inputs(self, pressed_key, alert_key=None):
        """Handle pressed key inputs and alert keys"""

        if not self.can_land:
            return

        thrust = None  # Set initially to None
        rotated = False  # Set to False because the starting angle is 0
        if alert_key != pygame.K_SPACE and pressed_key[pygame.K_SPACE]:
            # Show thrust image when 'space' is pressed
            thrust = EngineThrust(self.rect, self.angle)  # Become an instance of the 'EngineThrust' class only if the
            # the 'space' key is pressed
            self.start_engine()

        if alert_key != pygame.K_LEFT and pressed_key[pygame.K_LEFT]:
            # Rotate lander anticlockwise when 'left' is pressed
            self.angle += 1
            rotated = True  # Lander becomes rotated

        if alert_key != pygame.K_RIGHT and pressed_key[pygame.K_RIGHT]:
            # Rotate lander clockwise when 'left' is pressed
            self.angle -= 1
            rotated = True  # Lander becomes rotated

        if rotated:  # Create rotated Sprite
            self.rot_image = pygame.transform.rotate(self.image, self.angle)

        return thrust  # Return thrust Sprite if 'space' has been pressed else None
