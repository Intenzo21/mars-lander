from time import clock  # To show the time elapsed
from random import choice  # Used for the random alert key choice

from .lander_class import *
from .meteor_class import *


def init():
    """
    Initialize pygame, pygame font and set window caption
    """
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Mars Lander v1.0')


class MarsLanderGame:
    """
    CREATE GAME CLASS
    """

    def __init__(self, fps=30, width=1200, height=750):  # Weight and height of the game window
        self.screen = pygame.display.set_mode((width, height))  # Configures the game window size
        self.clock = pygame.time.Clock()  # Initialize clock
        self.FPS = fps   # Frames per second
        self.regular_font = pygame.font.SysFont('Comic Sans MS', 15)  # Create regular text font
        self.alert_font = pygame.font.SysFont('Comic Sans MS', 18)  # Create alert text font
        self.large_font = pygame.font.SysFont('Comic Sans MS', 50)  # Create large text font

        self.score = 0  # Holds the game score
        self.lives = 3  # Holds the number of lives the player has

        self.obstacles = pygame.sprite.Group()  # Create obstacle Sprite Group
        self.meteors = pygame.sprite.Group()  # Create meteor Sprite Group
        self.landing_pads = pygame.sprite.Group()  # Create landing pad Sprite Group
        self.background = Sprite('images/mars_background_instr.png', 0, 0)  # Create and place the background image

        self.lander = Lander(width)  # Generate the lander
        self.height = height  # Holds the height of the game window

        self.random_alert = None  # Holds random alert signal
        self.random_storm = None  # Carries random meteor storm time
        self.alert_key = None  # Holds random alert key

        # Create sprites for landing pads and add them to the pads group
        Sprite('images/pad.png', 732, randint(858, 1042)).add(self.landing_pads)
        Sprite('images/pad_tall.png', 620, randint(458, 700)).add(self.landing_pads)
        Sprite('images/pad.png', 650, randint(0, 300)).add(self.landing_pads)

        self.reset_obstacles()
        self.create_meteor_storm()
        self.create_alert_signal()

    @property
    def game_over(self):
        """
        Check if there are no lives left
        """
        return self.lives < 1

    def reset_obstacles(self):
        """
        Create obstacles at a fixed location and add them to the obstacles Group
        """

        self.obstacles.empty()  # Remove all Sprites from this Group.
        Sprite('images/pipe_ramp_NE.png', 540, 90).add(self.obstacles)
        Sprite('images/building_dome.png', 575, 420).add(self.obstacles)
        Sprite('images/satellite_SW.png', 435, 1150).add(self.obstacles)
        Sprite('images/rocks_ore_SW.png', 620, 1080).add(self.obstacles)
        Sprite('images/building_station_SW.png', 640, 850).add(self.obstacles)

    def create_meteor_storm(self, number_of_images=4):
        """
        Create meteors and add them to the meteors Group
        """

        now = int(clock())  # Take the elapsed time since the start of the game
        self.random_storm = randint(now + 3, now + 12)  # Randomize meteor rain time

        self.meteors.empty()  # Remove all Sprites from this Group.
        for i in range(randint(5, 10)):
            image_name = 'images/spaceMeteors_{}.png'.format(randint(1, number_of_images))
            Meteor(image_name, -2 * i * self.FPS, randint(300, 900)).add(self.meteors)

    def create_alert_signal(self):
        """
        Randomize alert signal and choose random alert key
        """

        self.random_alert = randint(int(clock() + 5), int(clock() + 15))
        self.alert_key = choice((pygame.K_SPACE, pygame.K_LEFT, pygame.K_RIGHT))

    def display_text(self, message, position, color=(255, 0, 0)):
        """
        Create new text and show it on the screen
        """

        text = self.regular_font.render(message, False, color)
        self.screen.blit(text, position)

    def run_program(self):
        """
        Run the program
        """

        meteor_storm = False  # Set to True whenever a storm should occur
        while not self.game_over:
            self.clock.tick(self.FPS)  # Frames per second

            # If the user clicks the 'X' button on the window it quits the program
            if any(event.type == pygame.QUIT for event in pygame.event.get()):
                return
            self.screen.fill([255, 255, 255])  # Fill the empty spaces with white color
            self.screen.blit(self.background.image, self.background.rect)  # Place the background image
            self.landing_pads.draw(self.screen)  # Draw the landing pads
            self.obstacles.draw(self.screen)  # Draw the obstacles on the screen

            # Check for collisions with obstacles and remove hit ones adding 10% damage for each one hit
            obstacles_hit = pygame.sprite.spritecollide(self.lander, self.obstacles, True)
            self.lander.damage += 10 * len(obstacles_hit)

            pressed_key = pygame.key.get_pressed()  # Take pressed key value

            if not meteor_storm and clock() > self.random_storm:
                # As soon as the clock passes the random storm time it causes meteor rain
                meteor_storm = True

            if meteor_storm:  # Draw meteors if 'meteor_storm' is set to True
                self.meteors.update()
                self.meteors.draw(self.screen)

                # Check for collisions with meteors and remove hit ones
                meteors_hit = pygame.sprite.spritecollide(self.lander, self.meteors, True)
                self.lander.damage += 25 * len(meteors_hit)

            if self.lander.damage > 100:  # Restrict the damage to 100 %
                self.lander.damage = 100

            if pressed_key[pygame.K_ESCAPE]:  # Stop game if the 'Esc' button is pressed
                return

            if self.random_alert < clock() < self.random_alert + 2:  # Show 2 second alert message when the clock
                # passes the random alert time
                alert_msg = self.alert_font.render('*ALERT*', False, (0, 0, 255))
                self.screen.blit(alert_msg, (190, 80))
                thrust = self.lander.handle_inputs(pressed_key, self.alert_key)
            else:
                thrust = self.lander.handle_inputs(pressed_key)
            if thrust:
                self.screen.blit(thrust.rot_image, thrust.rect)
            self.screen.blit(self.lander.rot_image, self.lander.rect)

            self.display_text('{:.1f} s'.format(clock()), (72, 10))  # Display clock in seconds
            self.display_text('{:.1f} m/s'.format(self.lander.veloc_y), (280, 56))  # Display y-axis velocity
            # (downward, meters per second)
            self.display_text('{:.1f} m/s'.format(self.lander.veloc_x), (280, 33))  # Display x-axis velocity (sideways,
            # meters per second)
            self.display_text('{:d} kg'.format(self.lander.fuel), (72, 33))  # Display remaining fuel in kg
            self.display_text('{:.0f} m'.format(self.lander.altitude), (280, 10))  # Display altitude in meters
            self.display_text('{} %'.format(self.lander.damage), (95, 56))  # Display damage suffered by the mars lander
            self.display_text('{:.0f} pts'.format(self.score), (77, 82))  # Display game score
            self.display_text('LIVES: {}'.format(self.lives), (285, 82), (255, 255, 0))  # Display player's lives left

            self.lander.free_fall()  # Call 'free_fall' method located in 'Lander' Sprite class
            pygame.display.update()

            landing_pad_reached = pygame.sprite.spritecollideany(self.lander, self.landing_pads)
            if landing_pad_reached or self.lander.rect.bottom > self.height:  # Create new alert, meteor storm time and
                # reset obstacles whenever the lander crashes or lands successfully on a landing pad
                self.create_alert_signal()
                self.create_meteor_storm()
                self.reset_obstacles()
                meteor_storm = False
                if landing_pad_reached and self.lander.rect.right < landing_pad_reached.rect.right and \
                        self.lander.rect.left > landing_pad_reached.rect.left and self.lander.has_landing_position():
                    self.score += 50
                    should_exit = self.show_message()
                else:
                    self.lives -= 1  # Decrement lives by 1 if the lander has crashed
                    should_exit = self.show_message('crashed')
                if should_exit:
                    return
                self.lander.reset_stats()  # Reset lander stats

    def show_message(self, msg=None):
        """
        Display crash or successful landing message in the middle of the screen and wait for a key to be pressed
        """

        if msg is not None:
            crash_msg = self.large_font.render('You Have Crashed!', False, (255, 0, 0))
            self.screen.blit(crash_msg, (420, 300))
        else:
            pts_msg = self.large_font.render('You Have Landed Successfully! +50 pts', False, (0, 180, 0))
            self.screen.blit(pts_msg, (160, 300))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit the game if the 'X' button is clicked
                    return True
                if event.type == pygame.KEYDOWN:  # Wait for a key to be pressed and if so resume the game
                    return False

            pygame.display.update()
            self.clock.tick(self.FPS)
