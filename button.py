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
        self.font = pygame.font.SysFont('Courier', 48)

        # Build the button's rect and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_message(msg)

        # Set the paused button's attributes.
        self.p_width, self.p_height = 200, 60
        self.p_button_color = (200, 50, 30)
        self.p_text_color = (0, 0, 0)
        self.p_font = pygame.font.SysFont('Forte', 60)

        # Build the button's rect and center it.
        self.p_rect = pygame.Rect(0, 0, self.p_width, self.p_height)
        self.p_rect.center = self.screen_rect.center

    def _prep_message(self, msg):
        """ Turn message into rendered text and center it on the button. """
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_play_button(self):
        """ Draw blank button and then draw the message. """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_paused_button(self):
        """ Non-clickable button that is drawn when the game is paused. """
        self.p_msg_image = self.font.render('Game Paused', True,
                                            self.p_text_color,
                                            self.p_button_color)
        self.p_msg_image_rect = self.p_msg_image.get_rect()
        self.p_msg_image_rect.center = self.screen_rect.center
        self.screen.fill(self.p_button_color, self.p_rect)
        self.screen.blit(self.p_msg_image, self.p_msg_image_rect)