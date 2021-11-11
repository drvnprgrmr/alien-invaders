class GameStats:
    """ Manage the statistics for alien inivasion. """
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ Reset the statistics of the game that can change during
        gameplay. """
        self.ships_left = self.settings.ship_limit
        # Start alien invasion in an active state.
        self.game_active = False
