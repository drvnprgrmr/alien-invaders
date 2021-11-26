class Settings:
    """ This class stores all the settings for pygame. """

    def __init__(self):
        """ Initialize the game's static settings. """
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (50, 50, 50)
        self.bullet_limit = 4

        # Alien Settings.
        self.fleet_drop_speed = 5
        self.score_scale = 1.5  # Rate at which the point's awarded for
                                # killing an alien increases.

        # Rate at which the game speeds up.
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize the game settings that will change over time. """
        self.alien_speed = 0.5
        self.ship_speed = 2.5
        self.bullet_speed = 1.0

        self.fleet_direction = 1  # 1 means right; -1 means left

        # Scoring.
        self.alien_points = 50

    def increase_speed(self):
        """ Increase the speed of the ship, aliens, and bullets. """
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
