import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialise ship and set starting position"""
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load image and get its rect
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at bottom centre of screen
        # attributes of rect: centre, top , bottom, left, right etc.
        # set ship's midbottom to match screen's midbottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ship's horizontal position
        self.x = float(self.rect.x) #assign to x as rect only keeps integer

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Update ship's position based on movement flag"""

        # update ship's x value, not the rect
        # limit rect's movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
         # if elif used, right key would have priority
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x
    
    def centre_ship(self):
        """Centre ship on screen"""
        #set ship to mid bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom 
        self.x = float(self.rect.x)
