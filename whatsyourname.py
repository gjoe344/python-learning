
firstname = 'Barack'
lastname = 'Obama'

def print_myname(firstname,lastname):
    '''
    This functions takes in two strings and prints out a message
    '''
    if isinstance(firstname, str) == True and isinstance(lastname, str) == True:

        return 'Hello ' + firstname + ' ' + lastname +'! You just delved into python'
    else:
        return 'Error: Not a String'

#print(print_myname(firstname,lastname))
print(print_myname(34, 3.45234))

# End of Lesson 3