import pygame.font


class Button():
    """Class representing a button"""

    def __init__(self, ai_game, msg):
        """Initialize button settings"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Define button size and style
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create and center button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Set message in button and center text"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw empty button and then messege"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)