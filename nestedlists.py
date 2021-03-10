records = [["chi",20.0], ["beta",50.0],["alpha",50.0], ["theta",80.0]]

def getMinValue(array):
    '''
    #abstracted boom*** This function returns min value from given list of numbers
    '''
    minValue = None
    for index, item in enumerate(array):
        if index == 0:
            value1 = item #grades[index]
        else:
            value2 = item
            if value1 > value2:
                minValue = value2
            elif value1 < value2:
                minValue = value1
            elif value1 == value2:
                minValue = value2
            value1 = minValue

    return minValue

def findLowestGrade(records):
    '''
    This function returns lowest grade given a record
    '''
    grades = []

    for item in records:
        name = item[0]
        grade = item[1]
        grades.append(grade)

    minValue = getMinValue(grades)
    
    for item in records:
        if item[1] == minValue: 
            lowestGradeName = item[0]

    return lowestGradeName

def findSecondLowestGrade(records):
    '''
    This function returns the second lowest grade given a record
    '''
    grades = []

    for item in records:
        name = item[0]
        grade = item[1]
        grades.append(grade) #populates grade list
    
    minValue = getMinValue(grades)
    grades.remove(minValue)

    secondLowestGrade = getMinValue(grades)

    return secondLowestGrade

print(findSecondLowestGrade(records))