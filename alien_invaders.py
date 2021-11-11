# External imports.
import sys
import pygame
from time import sleep

# Internal imports.
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """ Class modelling the game 'Alien Invaders'."""
    def __init__(self):
        """ Initialize the game and game attributes. """
        pygame.init()

        self.settings = Settings()

        ''' Full-screen settings'''
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # ''' If not in full-screen mode'''
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height)
        # )
        pygame.display.set_caption('Alien Invaders', 'AI')
        self.bg_color = self.settings.bg_color

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.stats = GameStats(self)

        self._create_fleet()

        # Create the play button.
        self.play_button = Button(self, 'Play')

    def _check_events(self):
        """ Helper method that checks for mouse clicks and key presses. """
        for event in pygame.event.get():
            # Watch for keyboard and mouse events.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button_clicked(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_button_clicked(self, mouse_pos):
        """ Start a new game if the button was clicked. """
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _check_keydown_events(self, event):
        """ Check for key presses. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Pressing 'q' to exit.
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Check for key releases. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create a bullet and add it to the 'bullets' group only if the
        bullets limit has not been exceeded. """
        if len(self.bullets.sprites()) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update the positions of bullets and get rid of bullets that have
        left the screen"""
        # Update the bullets.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ Respond to bullet-alien collisions. """
        # Check if the bullets have collided with any of the aliens, and if
        # so remove the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)

        # Destroy all remaining bullets and repopulate the fleet if all
        # aliens have been destroyed.
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """ Update the positions of the aliens on the screen. """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _create_fleet(self):
        """ Creates a fleet of aliens. """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Calculate the available space on the screen for drawing the aliens.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = (self.settings.screen_height -
                             self.ship.rect.height - 3 * alien_height)

        number_aliens_x = available_space_x // (2 * alien_width) + 1
        number_of_rows = available_space_y // (2 * alien_height)
        for row in range(number_of_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)

    def _create_alien(self, alien_number, row):
        """ Create an alien given the alien number and row. """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x = alien.rect.x
        alien.y = alien.rect.y
        alien.x = alien_width + alien_number * alien_width * 2
        alien.y = (row * alien_height * 2) + alien_height
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """ Check if the fleet has reached either end of the screen. """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Change the direction of the fleet. """
        for alien in self.aliens.sprites():
            alien.y += self.settings.fleet_drop_speed
            alien.rect.y = alien.y
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """ Respond to a ship being hit. """
        # Reduce the number of ships left.
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Clear all remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and recenter the ship.
            self._create_fleet()
            self.ship.recenter()

            # Pause the game for a little while.
            sleep(1.0)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """ Check if any aliens have reached the bottom of the screen. """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat it as if a ship has been hit.
                self._ship_hit()
                break

    def _update_screen(self):
        """ Helper method that updates the screen and all elements in it."""
        # Fill the screen with the set background color
        self.screen.fill(self.bg_color)

        # Draw the ship to the screen using updated values of it's
        # rect's position.
        self.ship.blitme()

        # Draw the bullets to the screen.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the fleet of aliens to the screen.
        self.aliens.draw(self.screen)

        # Draw the play button to the screen.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        """ Begin the main loop of the game. """
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
