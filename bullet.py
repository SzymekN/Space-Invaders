import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class controls bullets shoot by player"""

    def __init__(self, ai_game):
        """Create bullet at ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet at (0,0) and change its position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Convert bullet position to float
        self.y = float(self.rect.y)

    def update(self):
        """Change bullet position on screen"""
        # Update position value
        self.y -= self.settings.bullet_speed
        # Update object position
        self.rect.y = self.y

    def draw_bullet(self):
        """Show bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
