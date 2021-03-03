# Start of Lesson 2

#if else - do while(nope) - for loops - switch statements(nope) - conditions

my_list0 = [23, 1.5566, 'fruits', True]

num1 = 10
num2 = 5

#If statements
if num1 > num2:
    print('Num1 is greater than Num2')
if num1 == num2:
    print('Num1 is equal ')
if num1 < num2:
    print('Num1 is less than Num2')

#Operators
# > - greater than
# <= - greater than or equals to
# <= - less than or equal to
# < - less than
# == - equal to
# && / and - and
# || / or - or

#while loops
while num1 > num2:
    print(num2)
    num2 += 1

myfruit = ['apple', 'oragne', 'bananas']

#for loops
for item in myfruit:
    print(item)

#Using indexes
for index, item in enumerate(myfruit):
    print(index)
    print(item)    