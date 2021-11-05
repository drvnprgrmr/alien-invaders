# External imports.
import sys
import pygame

# Internal imports.
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Class modelling the game 'Alien Invaders'."""
    def __init__(self):
        """ Initialize the game and game attributes. """
        pygame.init()

        self.sett = Settings()

        self.screen = pygame.display.set_mode(
            (self.sett.screen_width, self.sett.screen_height)
        )
        pygame.display.set_caption('Alien Invaders', 'AI')
        self.bg_color = self.sett.bg_color

        self.ship = Ship(self)

    # noinspection PyMethodMayBeStatic
    def run_game(self):
        """ Begin the main loop of the game. """
        while True:
            for event in pygame.event.get():
                # Watch for keyboard and mouse events.
                if event.type == pygame.QUIT:
                    sys.exit()

            # Fill the screen with the set background color
            self.screen.fill(self.bg_color)

            # Draw the ship to the screen.
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
