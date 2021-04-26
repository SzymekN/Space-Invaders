class GameStats:
    """Keep track on statistics of Alien Ivaders game"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True
        

    def reset_stats(self):
        """Initialize default game data"""
        self.ships_left = self.settings.ship_limit