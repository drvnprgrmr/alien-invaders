import sys

import pygame


class AlienInvasion:
    """ Class modelling the game 'Alien Invaders'."""
    def __init__(self):
        """ Initialize the game and game attributes. """
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Alien Invaders', 'AI')

    def run_game(self):
        """ Begin the main loop of the game. """
        while True:
            # Display the most recent screen.
            pygame.display.flip()
            for event in pygame.event.get():
                # Watch for keyboard and mouse events.
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()