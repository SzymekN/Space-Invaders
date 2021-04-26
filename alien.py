import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class represents one alien enemy"""

    def __init__(self, ai_game):
        """Initialize enemy and its parameters"""
        super().__init__()
        self.screen = ai_game.screen

        #load image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #set enemy position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store exact enemy position
        self.x = float(self.rect.x)