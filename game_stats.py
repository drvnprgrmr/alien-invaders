class GameStats:
    """ Manage the statistics for alien inivasion. """
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        with open('highscore.txt', 'r') as hs:
            high_score = hs.read()
        self.high_score = int(high_score)
        self.reset_stats()

    def reset_stats(self):
        """ Reset the statistics of the game that can change during
        gameplay. """
        self.ships_left = self.settings.ship_limit

        # Start alien invasion in an inactive state.
        self.game_active = False

        self.game_paused = False
        self.level = 1
        self.score = 0

    def save_highscore(self, new_hs):
        """ Save the user's highscore to a file. """
        with open('highscore.txt', 'w') as hs:
            hs.write(str(new_hs))
