from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_10.txt'
inputName = 'Inputs/Input_2023_10.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
pipeArray = []
areaArray = []

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

# Create arrays
for lineNumber, line in enumerate(fileLines):
    pipeArray.append([pipe for pipe in line])
    areaArray.append(['.' for pipe in line])
    if 'S' in line:
        startPosition = lineNumber, line.index('S')

# Find total length of the loop
difference = 0, 1
pipePosition = [x for x in map(sum, zip(startPosition, difference))]
pipe = pipeArray[pipePosition[0]][pipePosition[1]]
areaArray[pipePosition[0]][pipePosition[1]] = 'X'
pathLength = 1

while pipe!='S':
    difference = pipeDict[(pipe, difference[0], difference[1])]
    pipePosition = [pipePosition[0] + difference[0], pipePosition[1] + difference[1]]
    pipe = pipeArray[pipePosition[0]][pipePosition[1]]
    areaArray[pipePosition[0]][pipePosition[1]] = 'X'
    pathLength += 1

endTime1 = timer()

print(int(pathLength/2))
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

startTime2 = timer()

numCards = [1]*len(fileLines)
sum2 = 0

# Change the map, so that every part of the loop is 'X' and every other part is '.'
# Done!

# Check whether left or right side is in the loop, when starting to the right from 'S'

# For every step through the loop, check the tile on your right
# Tiles to check, assuming we move CW:
# When moving up (down), check tile to the right (left)
# When moving right (left), check tile below (above)
# When taking a right corner, nothing to check
# When taking a left corner, check tile in front of you and to the right (from where you came from)


# If that area is not included yet (so not filled with 'O'), flood fill the area
# Fill whole area with 'O', keeping track of area, adding that to running tally
def flood_fill(point, array, fillValue='O'):
    """
    Fill the whole area enclosed by the borders in array, with point in it

    Inputs:
    point - tuple with grid coordinates (row, column)
    array - list of lists with 'X' borders, anything else not borders [['X', '.', ...], ...]
    *fillValue='O' - char to be used for filling area

    Outputs:
    filledArray - list of lists with 'X' as borders, fillValue as filled area

    Notes:
    Does not work properly if area is bordered by array edge
    """

    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # Includes all points in the area, for which neighbors are not yet checked
    pointSet = {point: None}

    # If point is not on a border, set it to fillValue
    if array[point[0]][point[1]]!='X':
        array[point[0]][point[1]] = fillValue

    # Continue with loop until pointSet is empty (all neighbors are checked)
    while pointSet:
        # Select last element from pointSet (DFS), delete it from pointSet
        tmpPoint = list(pointSet.keys())[-1]
        del pointSet[tmpPoint]

        # Check all four neighbors, if they are not 'X' set to fillValue, update pointSet
        for diff in neighbors:
            checkPoint = tmpPoint[0] + diff[0], tmpPoint[1] + diff[1]
            if array[checkPoint[0]][checkPoint[1]]!='X':
                array[checkPoint[0]][checkPoint[1]] = fillValue
                pointSet[checkPoint] = None
    
    return array

# Determine total number of enclosed tiles
# sum2 = 0
# for row in areaArray:
#     sum2 += row.count('O')

endTime2 = timer()

print(sum2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))