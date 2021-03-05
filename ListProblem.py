# Start of Lesson 3
bubbles = [1,2,3,4,5,6]
n = 9

def find(n,array):
    '''
    This function looks for n in a list
    '''
    for item in array:
        if item == n:
            return True
    return False   

print(find(n,bubbles))        

'''
index = 0
isFound = False

while isFound == False: 
    item = bubbles[index]
    if item == n:
        print('Found number in list')
        isFound = True #break
    else:
        print('No number found')
        if index == len(bubbles):
            isFound = True #break
    index = index + 1 # index += 1
'''