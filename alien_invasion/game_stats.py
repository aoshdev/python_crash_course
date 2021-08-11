class GameStats:
    """Track stats for alien invasion"""

    def __init__(self, ai_game):
        """Initialise stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False # start in inactive state

        # high score should never be reset
        self.high_score = 0
    
    def reset_stats(self):
        """Initialise stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
