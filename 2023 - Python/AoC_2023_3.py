from timeit import default_timer as timer
import re

startTime1 = timer()

testName = 'Tests/Test_2023_3.txt'
inputName = 'Inputs/Input_2023_3.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

# Generate array (with padding) as list of lists
array = ['.' + line + '.' for line in fileLines]
array.insert(0, '.'*len(array[0]))
array.insert(len(array), '.'*len(array[0]))

# Initialize array with zeros for part II
numIDarray = [[0 for col in row] for row in array]

sum1 = 0
numID = 1
d = dict()

for lineNumber, line in enumerate(array):
    numbers = {el for el in re.split('[^0-9]', line) if el.isdigit()}

    tmp = 0

    for number in numbers:
        idxs = [m.span() for m in re.finditer(number, line)]

        for idxStart, idxEnd in idxs:
            if not line[idxStart-1].isdigit() and not line[idxEnd].isdigit():
                region = [row[idxStart-1:idxEnd+1] for row in array[lineNumber-1:lineNumber+2]]
                numCheck = [x for line in region for x in line if not x.isdigit() and not x=='.']

                if numCheck:
                    sum1 += int(number)

                numIDarray[lineNumber][idxStart:idxEnd] = [numID]*(idxEnd - idxStart)
                d[numID] = number
                numID += 1

endTime1 = timer()

print(sum1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

startTime2 = timer()

sum2 = 0

for lineNumber, line in enumerate(array):
    idxs = [m.start() for m in re.finditer('\*', line)]

    for idx in idxs:
        numIDs = {i for row in numIDarray[lineNumber-1:lineNumber+2] for i in row[idx-1:idx+2]}

        sortedIDs = sorted(numIDs)

        if len(sortedIDs)==3:
            sum2 += int(d.get(sortedIDs[1]))*int(d.get(sortedIDs[2]))

endTime2 = timer()

print(sum2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))