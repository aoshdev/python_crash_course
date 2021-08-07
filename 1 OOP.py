# Ch9: classes
# ============================================================

# creating a dog class
class Dog:
    """A simple model of a dog."""

    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self): # these functions are called methods
        """Simulate a dog sitting in response to a command."""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Simulate rolling over"""
        print(f'{self.name} rolled over!')


# making an isntance from a class

my_dog = Dog('Will', 5)
print()
my_dog.name #use dot notation to access attributes
my_dog.age

my_dog.sit() #use dot notation to call methods
my_dog.roll_over()



# example

class Restaurant:
    """A restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes to describe restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print names"""
        print(f'{self.restaurant_name} and {self.cuisine_type}')
    
    def open_restaurant(self):
        """Open"""
        print('Open!')

kfc = Restaurant('carlo', 'chicken')
kfc.describe_restaurant()
kfc.open_restaurant()


# modifying attributes (3 ways)

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

first_car = Car('audi','r8',2019)
first_car.get_description()
first_car.read_odometer()


first_car.odometer_reading = 10 #directly changing the attribute
first_car.read_odometer()

first_car.update_odometer(8) #modify via a method
first_car.read_odometer()

first_car.increment_odometer(2) #increment via a method
first_car.read_odometer()



# inheritance
# creating a new 'child' class based on a 'parent' class

class ElectricCar(Car): # MUST include parent class in brackets
    """represents just electric cars"""

    def __init__(self, make, model, year):
        """initialise attribtues of the parent class"""
        # super() allows you to call methods from parent class
        # superclass is parent, subclass is child
        super().__init__(make, model, year)

        # can also define additional attributes
        self.battery_size = 75
    

    # if parent class had describe_battery() method, this would override it
    def describe_battery(self):
        """this describes battery status"""
        print(f'This car has a {self.battery_size}kwH battery.')
    
my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.get_description()
my_tesla.describe_battery()


# breaking up class into smaller classes
# i.e. assigning classes to an attribute

class Battery:
    """a model for batteries"""

    def __init__(self, battery_size = 75):
        """initialise battery attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print descriptions"""
        print(f'Battery size: {self.battery_size}')

class ElectricCar(Car):
    """represent electric cars"""

    def __init__(self, make, model, year):
        """initialise attributes"""
        super().__init__(make,model,year)
        self.battery = Battery() #assigns Battery() instance to attribute
        # now ElectricCar() instance will also have Battery() instance

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()


# importing from module

from car import Car

my_new_car = Car("Tesla","Model S", 2021)
my_new_car.read_odometer()