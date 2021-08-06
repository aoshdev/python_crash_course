# Ch1 - skipped -
# ============================================================


# Ch2: variables and simple data types
# ============================================================

# concatenate strings
first = 'abc'
second = 'def'
combined = f'{first} {second}'
print(combined)

combined = f'Hi, \n{first.title()}!'
print(combined)

# quotes
print("Mike's message with an apostrophe")

# numbers
long_number = 14_000_000_000 #python ignores _, makes it more readable

# multiple assignment
x, y, z = 1, 2, 3


# Ch3: lists
# ============================================================

cars = ['a','b','c']
cars[0] = 'd'
cars

cars.append('e')
cars

cars.insert(0, 'first')
cars

# removing from list
del cars[1]
cars

cars.remove('first') # removes only the first occurence in list



# remove last item in list and stores it 
cars = ['a', 'b', 'c']
cars_popped = cars.pop()
cars
f'Last car was {cars_popped}'

# remove any item in list
cars_popped1 = cars.pop(1)
cars

# sort
bikes = ['g', 'a', 'd']
bikes.sort() # sorts permanently
print(bikes)

print(sorted(bikes)) # sorts temporarily

# other
bikes.reverse() # reverse order
print(bikes)

len(bikes)

# Ch4: lists still
# ============================================================

for value in range(1,5): # range stops at the last item and does not include it
    print(value)

list_of_numbers = list(range(1,5))
list_of_numbers1 = list(range(1,11 ,2))

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

# list compression
squares1 = [value**2 for value in range(1,11)] # [expression for-lopp]

# slicing
players = ['a','b','c','d']
print(players[0:3])
print(players[-3:]) #print last 3

# copying
list_a = ['a','b','c']
list_b = list_a[:]   #need to use a slice to COPY the list

list_a.append('d')
list_b.append('e')

print(list_a)
print(list_b)

list_c = list_b    #this does NOT copy. It points list_c to the same list as list_b
list_c.append('f')
print(list_b)

# tuples (these are immutable lists. Used to store values that do not change.)
dim = (20,30)

for i in dim:
    print(i)


# Ch5: if statements
# ============================================================

age_0 = 10
age_1 = 12

age_0 > 8 and age_1 > 5
age_0 > 8 or age_1 > 5

# check value exists in list
'a' in list_a

# checking plain list
list_d = []

if list_d:
    print('contains values')
else:
    print('empty')


# Ch6: dictionaries
# ============================================================

alien_0 = {'color':'green', 'points':5} # key:value
print(alien_0['points'])

# adding to dictionaries
alien_0['position'] = 25
print(alien_0)

# deleting
del alien_0['points']
print(alien_0)

# good practice to leave comma at last line
new_dict = {
    'a':1,
    'b':2,
}

# use get to print a message if missing key
alien_0['points']
alien_0.get('points', 'Missing points')

# loop dictionary
for key, value in alien_0.items(): #.items() returns a list of key-value pairs
    print('key\n')
    print('value\n')

for key in alien_0.keys(): #.keys() returns list of just keys
    print(key)

for key in alien_0: #default of looping a dictionary returns the keys
    print(key)
    print(alien_0[key])

for key in alien_0.values(): #.values() returns list of just values
    print(key)

# set makes a list unique. note that sets are also wrapped in braces
# sets do not retain items in any specific order
list_dup = ['a','b','b','c']
set(list_dup)

example_set = {'a','b','c'}


# dictionaries in list
alien_1 = {
    'a': 0,
    'b': 1,
}

alien_list = []
for i in range(10):
    alien_list.append(alien_1)

# lists in dictionary
pizza = {
    'crust': ['thick'],
    'toppings': ['mushrooms', 'cheese'],
}

for key, value in pizza.items():
    print(f'{key} is')
    for i in value:
        print(f'{i}')


# Ch7: user inputs and while loops
# ============================================================

message = input('input something:')
print(message)

# while loops
current = 1
while current <= 5:
    print(current)
    current += 1

# while with lists
start = ['a','b','c']
end = []

while start:
    temp = start.pop()

    print(temp)
    end.append(temp)

print(end)

# removing all occurences in list
long_list = ['a','b','c','a','b','c']

while 'a' in long_list:
    long_list.remove('a')

# using flags to stop while loops and filling dictionary
responses = {}

active = True

while active:
    name = input('name: ')
    value = input('value: ')

    responses[name] = value

    repeat = input('repeat? y/n')

    if repeat == 'n':
        active = False

# Ch8: functions
# ============================================================

# optional arguments/parameters
#set equal to '' or None and move to end of arguments

def get_formatted_name(first, last, middle=None):
    """Return full name"""
    if middle:
        full = f'{first} {middle} {last}'
    else:
        full = f'{first} {last}'

    return full.title()

test = get_formatted_name('bob','ann','con')
test


# passing an arbitrary number of arguements
# *args tells python to create tuple using the passed arguments
# *args must go last in arguments
def make_pizza(size, *toppings):
    print(f'Require the following for {size} pizza:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza(16, 'a','b')



# arbitrary number of arguments with dictionaries
# **kwargs creates an empty dictionary called kwargs
# (keyword args)

def profile(first, last, **info):
    info['first name'] = first
    info['last name'] = last

    return info

test = profile('a','b',c='d', e='f')
print(test)

# importing modules
import functions #save a file with functions ending in .py (these are 'modules')
functions.print_title('lol') #module_name.function_name()

# import modules using an alias
import functions as fn
fn.print_title('lols')

# import specific functions
#no need to use module_name since we've explicitly called this function
from functions import print_title
print_title('test') 

# import all functions in module
# not the best approach if importing large module where names may overlap
# with your own code
# best to import specific functions or use dot notation
from functions import *
print_title('LOL')

# give functions alias
from functions import print_title as pt
pt('17')