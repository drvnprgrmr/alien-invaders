import pygame.font


class Button:
    """ Creates a button with a message displayed on it. """

    def __init__(self, ai_game, msg):
        """ Initialize the message. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Set the button's attributes.
        self.width, self.height = 200, 50
        self.button_color = (0, 200, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_message(msg)

    def _prep_message(self, msg):
        """ Turn message into rendered text and center it on the button. """
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        """ Draw blank button and then draw the message. """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)