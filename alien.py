import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class represents one alien enemy"""

    def __init__(self, ai_game):
        """Initialize enemy and its parameters"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # set enemy position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store exact enemy position
        self.x = float(self.rect.x)

    def update(self):
        """Alien movement"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if some alien hit edge of a screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
