from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_3.txt'
inputName = 'Inputs/Input_2023_3.txt'

with open(testName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

# Generate array as list of lists
array = [line for line in fileLines]

# Add padding?


sum1 = 0

for lineNumber, line in enumerate(array):
    numbers = [el for el in line.split('.') if el.isdigit()]

    for number in numbers:
        idxStart = line.find(number)
        idxEnd = idxStart + len(number)

        # For every number that is found, check if there is a symbol (non-digit and not a period)
        region = [row[idxStart-1:idxEnd+1] for row in array[lineNumber-1:lineNumber+2]]
        
        numBool = [x for x in region if not x.isdigit() and not x=='.']

        # If so, add number to total
        if numBool:
            sum1 += int(number)

endTime1 = timer()

print(sum1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

startTime2 = timer()

endTime2 = timer()

print(sum2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))