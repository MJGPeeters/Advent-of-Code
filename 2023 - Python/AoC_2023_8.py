from timeit import default_timer as timer
import math as m

startTime1 = timer()

testName = 'Tests/Test_2023_8.txt'
inputName = 'Inputs/Input_2023_8.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

directionDict = dict()

for lineNumber, line in enumerate(fileLines):
    if lineNumber==0:
        directions = line
    elif lineNumber>1:
        tmp = line.split()
        directionDict[tmp[0]] = tmp[2][1:4], tmp[3][0:3]
 
directions = directions.replace('L', '0')
directions = directions.replace('R', '1')
numDirections = len(directions)

element = 'AAA'
stepNum = 0

while element!='ZZZ':
    element = directionDict[element][int(directions[stepNum % numDirections])]
    stepNum += 1

endTime1 = timer()

print(stepNum)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

startTime2 = timer()

stepNums = []

# Find all elements '**A'
elements = [element for element in directionDict.keys() if element[2]=='A']

# While not all elements are '**Z', choose next element for every element
for element in elements:
    stepNum = 0
    while element[2]!='Z':
        element = directionDict[element][int(directions[stepNum % numDirections])]
        stepNum += 1
    stepNums.append(stepNum)

stepNum = m.lcm(*stepNums)

endTime2 = timer()

print(stepNum)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))