class Settings:
    """ This class stores all the settings for pygame. """
    def __init__(self):
        """ Initialize all the game's settings. """
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed = 2.5
        self.ship_limit = 3
        
        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (50, 50, 50)
        self.bullet_limit = 4

        # Alien Settings.
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1  # 1 means right; -1 means left

