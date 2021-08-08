class Settings:
    """Store all settings here"""

    def __init__(self):
        """Initialise the game's settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5