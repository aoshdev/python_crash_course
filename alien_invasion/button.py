import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Initialise button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set dimensions and property of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #None=default font, 48 = size

        # Bbuild button's rect object and centre it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center #set to centre of screen

        # the button needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """turn msg into a rendered image and centre text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color) # turns text to image and store it
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect) # draws rectangle
        self.screen.blit(self.msg_image, self.msg_image_rect) # adds text image