import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to manage the alien's attributes and functions. """

    def __init__(self, ai_game):
        """ Initialize the alien's attribytes. """
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Load the alien's image and get it's rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """ Check if an alien has reached either edge. """
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """ Move the fleet. """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x