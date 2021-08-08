"""Class used to represent a car"""

class Car:
    """Represent a car"""

    def __init__(self, make, model, year):
        """Initialise attributes to describe car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting default value
    
    def get_description(self):
        """Format name"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Print odometer"""
        print(f'{self.odometer_reading}km')

    def update_odometer(self, mileage):
        """
        update km travelled
        reject if anyone tries to rollback
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back")
    
    def increment_odometer(self, miles):
        """add an amount to odometer"""
        self.odometer_reading += miles