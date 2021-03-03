# practice problem
n = 24 # 1 <= n <= 100


if n%2 != 0: #when n is odd
    print('Weird')
   # if n >= 6 and n <= 20: 
    #    print('Weirder')

if n%2 == 0 and n >= 2 and n <= 5: #when n is even and inclusive range of 2 - 5
    print('Not Weird')

if n%2 == 0: #when n is even
    if n >= 6 and n <= 20: #when n is inclusive range 6 - 20
        print('Weird')

if n%2 ==0:
    if n > 20: # when n is even and greater than 20
        print('Not Weird')

#End of Lesson 2