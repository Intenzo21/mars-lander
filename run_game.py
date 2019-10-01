"""
Main function to run the game.
"""

from classes.game_class import *

if __name__ == '__main__':
    init()  # Call pygame initializer function
    game = MarsLanderGame()  # Create MarsLander (game) instance
    game.run_program()  # Call 'run' method in order to run the program
    pygame.quit()  # Quit game
