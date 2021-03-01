# 1. comments - done by hashtags
"""
    this is
    a
    multiline comment 
"""
# 2. Printing
# String
print('My String')
# Integer
print(32)
# Float
print(1.111)

# Nesting functions
my_number = 10
values = type(my_number)
print(values)

# 3. Variables
# Integers, strings, booleans, Floats, Lists(array), Tuples, Objects
my_int = 20
print(type(my_int))
my_float = 20.222
print(type(my_float))
my_string = 'Jose is learning Python!'
print(type(my_string))

my_boolean = True # or False
print(my_boolean)
print(type(my_boolean))

my_list = [1,2,3,4,5]
my_list = [2, 3.44, 'Hey', True, [1,2,3]] #Dynamic, can contain a different variables
print(my_list)
print(type(my_list))
#Adding something into the list
variable = 'ME'
my_list.append(variable)
print(my_list)
print(type(my_list))
#Checking for length of an array
print(len(my_list))
#Indexing - retrieve Hey
print(my_list[2])
#Removing values from list
#Delete by indexing
my_list.pop(1)
print(my_list)
#Delete by value
my_list.remove('Hey')
print(my_list)

'''
Other things you can do with an array
append()    Adds an element at the end of the list
clear()    Removes all the elements from the list
copy()    Returns a copy of the list
count()    Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()    Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()    Removes the element at the specified position
remove()    Removes the first item with the specified value
reverse()    Reverses the order of the list
sort()    Sorts the list

'''

#Tuples 
my_tuple = ('apple', 'orange', 'blueberry', 1, 1.22)
print(type(my_tuple))
print(my_tuple)
#check lenth of tuple
print(len(my_tuple))
#cannot add anything anymore after being defined

#Objects 
#car = Car()
#print(type(car))
#my_list.append(car)
