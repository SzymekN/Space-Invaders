class Settings:
    def __init__(self):
        """Initialize game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.0
        self.ship_limit = 3

        # bullets settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # 1 -> fleet goes right, -1 fleet goes left
        self.fleet_direction = 1

        # game speed
        self.speedup_scale = 1.05
        self.score_scale = 1.5

        # score
        self.alien_points = 50
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that will chagne while playing game"""
        self.bullet_speed = 1.5
        self.ship_speed = 1.0
        self.alien_speed = 0.5

        self.fleet_direction = 1

    def increase_speed(self):
        """Increase game speed and scored points"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        

    
