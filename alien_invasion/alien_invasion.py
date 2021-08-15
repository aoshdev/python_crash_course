import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

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

        # create instance to store game stats and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # self here refers to current instance of AlienInvasion
        # this gives Ship access to resources e.g. screen
        self.ship = Ship(self) 
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group() # groups automatically draw

        self._create_fleet() #here cos its required before game starts?

        # make play button
        self.play_button = Button(self, "Play")


    # this method will control the game
    def run_game(self):
        """Start main loop for game"""
        while True:
            self._check_events() # refactored here to simplify

            if self.stats.game_active:
                self.ship.update() # position updated after checking key press
                self.bullets.update() # update position of bullet
                self._update_bullets()
                self._update_aliens()            
           
            self._update_screen() # Redraw screen

    def _check_events(self):
        """Response to keypresses and mouse events"""
        # an event loop to watch for keyboard and mouse
        for event in pygame.event.get(): #list of events 
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN: # for clicks
                mouse_pos = pygame.mouse.get_pos() # get x,y coord of click
                self._check_play_button(mouse_pos) # send to this method

            elif event.type == pygame.KEYDOWN: #any key pressed
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP: #when key is released
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start new game when player clicks play"""
        # if mouse overlaps with play button rect
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # only checks if game is not active
        if button_clicked and not self.stats.game_active:
            self.settings.initialise_dynamic_settings() # reset to base stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score() # updates score to 0 for new games
            self.sb.prep_level() #update level for new games
            self.sb.prep_ships() # draw ships

            # remove aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create new fleet and centre ship
            self._create_fleet()
            self.ship.centre_ship()

            # hide mouse cursor
            pygame.mouse.set_visible(False)

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
    
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet alien collisions"""
        # check if any bullets have hit aliens, if so remove both
        # groupcollide() 
        #   - checks for collision between 2 groups
        #   - creates a ky value pair (key = bullet, value = alien)
        #   - arguments for removing each element
        collisions = pygame.sprite.groupcollide( 
            self.bullets, self.aliens, True, True
        )

        if collisions:
            # in case multiple aliens are hit in same loop
            # each value is a list of aliens hit by a single bullet
            for aliens in collisions.values(): 
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score() #updates image
            self.sb.check_high_score() #check everytime there's a hit

        if not self.aliens: # see if aliens group is empty
            # destroy existing bullets and create new fleet
            self.bullets.empty() # .empty() removes all sprites from group
            self._create_fleet()
            self.settings.increase_speed()

            # increase level
            self.stats.level += 1
            self.sb.prep_level() # update image

    def _update_aliens(self):
        """
        Check if fleet at edge and 
        update the positions of all aliens in the fleet
        """
        self._check_fleet_edges()
        self.aliens.update() # used on aliens group which calls every alien

        # look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hitting bottom of screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            # Decrement ships left
            self.stats.ships_left -= 1
            self.sb.prep_ships() # update number of ships drawn


            # Remove remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and centre the ship
            self._create_fleet()
            self.ship.centre_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True) # reappears when game ends
    
    def _create_fleet(self):
        """Create fleet of aliens"""
        # Make an alien
        alien = Alien(self) # only used for calculations and not added to fleet
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine number of rows of aliens
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create full fleet of aliens
        for row_number in range(number_rows):
            # create first row of aliens
            for alien_number in range(number_aliens_x):
                # create alien and place it in row
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create alien and place in row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # each new alien is positioned to the right of previous
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x # set position of rect
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien) # add to group of aliens

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break # exit for loop
    
    def _change_fleet_direction(self):
        """Drop entire fleet and change fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat same as if ship was hit
                self._ship_hit()
                break # break loop as soon as 1 is hit

    def _update_screen(self):
        """Update images on screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() # draw ship on top of background

        # bullets.sprites() returns a list of all sprites in bullets group
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen) #.draw is a method in sprites

        # draw score info
        self.sb.show_score()

        # draw play button if game is inactive
        # last so that it is on top of the other objects on screen
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__': # only runs if this file is called directly
    # make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()


