import sys
import pygame

from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
from alien_invasion.bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """initalise the game and create game resources"""
        pygame.init()
        self.settings = Settings() # create instance of Settings
        
        # fullscreen
        # rectangle of screen: self.screen.get_rect()
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        ) # set display size
        pygame.display.set_caption('Alien Invasion')

        # self here refers to current instance of AlienInvasion
        # this gives Ship access to resources e.g. screen
        self.ship = Ship(self) 
        self.bullets = pygame.sprite.Group() 


    # this method will control the game
    def run_game(self):
        """Start main loop for game"""
        while True:
            self._check_events() # refactored here to simplify
            self.ship.update() # position updated after checking key press
            self.bullets.update() # update position of bullet
            self._update_bullets()            
            self._update_screen() # Redraw screen

            # Make most recently drawn screen visible
            pygame.display.flip()
    
    def _check_events(self):
        """Response to keypresses and mouse events"""
        # an event loop to watch for keyboard and mouse
        for event in pygame.event.get(): #list of events 
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN: #any key pressed
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP: #when key is released
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT: #K_RIGHT is right arrow key
            #move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #q key
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self,event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet and add to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self) #create instance of Bullet
            self.bullets.add(new_bullet) #add to group of bullets

    def _update_bullets(self):
        # get rid of bullets that disappear
        # can't remove from a list you're looping so loop a copy instead
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) # use to check bullets is being deleted
        
    def _update_screen(self):
        """Update images on screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() # draw ship on top of background

        # bullets.sprites() returns a list of all sprites in bullets group
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

if __name__ == '__main__': # only runs if this file is called directly
    # make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

