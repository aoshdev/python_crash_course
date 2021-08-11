import pygame.font
from pygame.sprite import Group

from alien_invasion.ship import Ship

class Scoreboard:
    """A class to report scoring info"""

    def __init__(self, ai_game):
        """Initialise scorekeeping attributes"""
        self.ai_game = ai_game # assign game instance to attribute
        self.screen = ai_game.screen #ai_game req. to access other objects
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings 
        self.stats = ai_game.stats

        # font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48) #instantiate font object

        # prepare initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

        self.prep_ships()

    def prep_score(self):
        """Turn score into rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score) # formats rstring to add commas
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color) #render score
        
        # display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score, level and ships to screen"""
        # draw image at coord
        self.screen.blit(self.score_image, self.score_rect) 
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn high score into image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)

        # centre high score at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx  = self.screen_rect.centerx
        self.high_score_rect.y = self.screen_rect.top

    def check_high_score(self):
        """Check if new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score # update high score
            self.prep_high_score() # update high score's image

    def prep_level(self):
        """Turn level into image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
            self.text_color, self.settings.bg_color)
        
        # position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right # right align with score
        self.level_rect.top = self.score_rect.bottom + 10 # under score

    def prep_ships(self):
        """Show how many ships are left"""

        self.ships = Group() # create empty group to hold instances
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)