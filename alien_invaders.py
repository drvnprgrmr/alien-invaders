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

        ''' Full-screen settings'''
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        ''' If not in full-screen mode'''
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Check for key presses. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Pressing 'q' to exit.
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ Check for key releases. """
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
