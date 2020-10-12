#fundamental data types
int
float
bool
str
list
tuple
set
dict

#Classes -> custom types

#Specialized data types

None - data type for no value

#Functions and some build it functions

type - gives you info about data type
round - math build in function gives us round numbers from float etc.
----------------------------------------------------------------------------
# """Simple birth_year calculator"""

birth_year = input('Whats you birth year?: ') # input is consider as a string!

curent_year = 2020

calc = curent_year - int(birth_year)

print(f'\nYour\n are\n {calc}\n old!') 

----------------------------------------------------------------------------
# """Simple password lenght and hiden display"""

name = input('What is your name?: ')

password = len(input('Enter password?: '))

PASS_SHOW = password * '*'  # Constant always show '*'

print(f'Hi {name} your password: {PASS_SHOW} is {password} charcater long!')
----------------------------------------------------------------------------
"""Lists"""

# List slicing, strings in list can be mutable
shoping_chart = [
  'Milk',
  'Bread',
  'Suncream'
]

shoping_chart[0] = 'Glass' # Changing first article
print(shoping_chart)

"""MATRIX multiple lists"""

matrix = [
   [1,2,3],
   [7,4,1],
   [a,b,c]
]
print(matrix[0][2])
----------------------------------------------------------------------------
""""""
















