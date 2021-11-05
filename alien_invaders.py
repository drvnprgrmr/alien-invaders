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

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invaders', 'AI')
        self.bg_color = self.settings.bg_color

        self.ship = Ship(self)

    def _check_events(self):
        """ Helper method that checks for mouse clicks and key presses. """
        for event in pygame.event.get():
            # Watch for keyboard and mouse events.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """ Helper method that updates the screen and all elements in it."""
        # Fill the screen with the set background color
        self.screen.fill(self.bg_color)

        # Draw the ship to the screen using updated values of it's
        # rect's position.
        self.ship.update()
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """ Begin the main loop of the game. """
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
