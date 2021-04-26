import pygame


class Ship:
    """Control the the spaceship"""

    def __init__(self, ai_game):
        """Initialize space ship and its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load image of spaceship and get its rect
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()

        # initialize all new ships at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # convert int to float to change position
        self.x = float(self.rect.x)

        # move flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship location"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # change position based on self.x
        self.rect.x = self.x

    def blitme(self):
        "Display ship at its current position"
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Move ship to center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
