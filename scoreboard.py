import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """ Class to manage the player's live scores and highscore. """

    def __init__(self, ai_game):
        """ Initialize score-keeping attributes. """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font characteristics.
        self.color = (30, 30, 30)
        self.hs_color = (0, 0, 160)
        self.font = pygame.font.SysFont('Courier', 20)

        self.prep_images()

    def prep_score(self):
        """ Render the Score as an image. """
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.color)

        # Display the score at the top right corner of the screen.
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20

    def prep_high_score(self):
        """ Load the high score. """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: " "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.hs_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx

    def check_high_score(self):
        """ Check to see if there is a new high score. """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score

    def prep_level(self):
        """ Render the current level as an image and set it's position. """
        level_str = "Level: " + str(self.stats.level)
        self.level_img = self.font.render(level_str, True, self.color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_ships(self):
        """ Prep the visual representation of ship's left. """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = ship_number * ship.rect.width
            ship.rect.y = 0
            self.ships.add(ship)

    def show_scoreboard(self):
        """ Draw the scores and level and ship's left to the screen. """
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

    def prep_images(self):
        self.prep_ships()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
