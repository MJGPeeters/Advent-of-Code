from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_10.txt'
inputName = 'Inputs/Input_2023_10.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
pipeArray = []

# Create dictionary with allowed moves for each pipe
pipeDict = {
    ('|', -1, 0): (-1, 0), 
    ('|', 1, 0): (1, 0),
    ('-', 0, 1): (0, 1),
    ('-', 0, -1): (0, -1),
    ('L', 1, 0): (0, 1),
    ('L', 0, -1): (-1, 0),
    ('J', 1, 0): (0, -1),
    ('J', 0, 1): (-1, 0),
    ('7', -1, 0): (0, -1),
    ('7', 0, 1): (1, 0),
    ('F', -1, 0): (0, 1),
    ('F', 0, -1): (1, 0),
}

# Create array
for lineNumber, line in enumerate(fileLines):
    pipeArray.append([pipe for pipe in line])
    if 'S' in line:
        startPosition = lineNumber, line.index('S')

# Find total length of the loop
difference = 0, 1
pipePosition = [x for x in map(sum, zip(startPosition, difference))]
pipe = pipeArray[pipePosition[0]][pipePosition[1]]
pathLength = 1

while pipe!='S':
    difference = pipeDict[(pipe, difference[0], difference[1])]
    pipePosition = [x for x in map(sum, zip(pipePosition, difference))]
    pipe = pipeArray[pipePosition[0]][pipePosition[1]]
    pathLength += 1

endTime1 = timer()

print(int(pathLength/2))
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# # Part II

# startTime2 = timer()

# numCards = [1]*len(fileLines)
# sum2 = 0



# print(sum2)
# print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))