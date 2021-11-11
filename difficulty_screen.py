import pygame.font


class DiffScreen:
    """ Manages the difficulty screen that appears when a player clicks
    'play'. """

    def __init__(self, ai_game):
        """ Draw the difficulty screen. """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.color = (255, 255, 255)

        # Set the fonts of all the texts in the difficulty screen.
        self.title_font = pygame.font.SysFont(None, 100, True)
        self.title_img = self.title_font.render('Choose a difficulty level.',
                                           True, self.color)
        self.title_rect = self.title_img.get_rect()
        self.title_rect.midtop = self.screen_rect.midtop

        self.easy = pygame.font.SysFont(None, 60, italic=True)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_img, self.title_rect)
        pygame.display.flip()