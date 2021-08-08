"""
Ch10: files and exceptions
"""

#connection to file is only open within 'with' statement
with open('pi_digits.txt') as file_object: 
    contents = file_object.read()
print(contents)

# read line by line
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# make list of lines from file
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() # removing white space and get into 1 string

print(f'Pi to 6 decimal places {pi_string[:8]}')



# writing to a file using open()
# default is 'r' read only. others are: 'w' write, 'a' append

filename = 'programming.txt'

with open(filename, 'w') as file_object: # 'w' for write mode
    file_object.write("Some message \n")
    file_object.write("Another message") 



# exceptions
# use these to prevent crashes and stops user seeing errors

print("Provide 2 numbers and I'll divide")
print("Enter 'q' to quit")

while True:
    first = input("\n First number: ")
    if first == 'q':
        break
    second = input("\n Second number: ")
    if second == 'q':
        break
    try:
        answer = int(first)/int(second) # only place code that might error here
    except ZeroDivisionError:
        print("Can't divide by zero!")
        # pass
        # can use 'pass' to act as a placeholder and do nothing
    else:
        print(answer) #rest of the code goes here
    print(answer)


# storing data using json
# a simple way to store python data structures and to share data

import json

numbers = [2,3,5,6,7,8,11,1236]

filename = 'numbers.json'
with open(filename, 'w') as f: # f is standard notation here
    json.dump(numbers, f)

with open(filename) as f:
    numbers_load = json.load(f)

print(numbers_load)










