from timeit import default_timer as timer

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

    # If point is not on a border, set it to fillValue. If it is on a border, return
    if array[point[0]][point[1]]!='X':
        array[point[0]][point[1]] = fillValue
    else:
        return array

    # Continue with loop until pointSet is empty (all neighbors are checked)
    while pointSet:
        # Select last element from pointSet (DFS), delete it from pointSet
        tmpPoint = list(pointSet.keys())[-1]
        del pointSet[tmpPoint]

        # Check all four neighbors, if they are not 'X' or fillValue set to fillValue, update pointSet
        for diff in neighbors:
            checkPoint = tmpPoint[0] + diff[0], tmpPoint[1] + diff[1]
            if array[checkPoint[0]][checkPoint[1]]!='X' and array[checkPoint[0]][checkPoint[1]]!=fillValue:
                array[checkPoint[0]][checkPoint[1]] = fillValue
                pointSet[checkPoint] = None
    
    return array

def clockwise_check(inDirection, outDirection):
    """
    Check whether a turn is clockwise or counterclockwise

    Inputs:
    inDirection - tuple describing incoming direction (drow, dcolumn)
    outDirection - tuple describing outgoing direction (drow, dcolumn)

    Outputs:
    1 if clockwise, -1 if counterclockwise
    """

    CW = 1
    CCW = -1

    if inDirection[0]==0:
        return CCW if (inDirection[1] + outDirection[0])==0 else CW 
    else:
        return CW if (inDirection[0] + outDirection[1])==0 else CCW 

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
        startPos = lineNumber, line.index('S')

# Find total length of the loop
diff = 0, 1
pathLength = 1
clockwiseCheck = 0
pathList = []

pipePos = [x for x in map(sum, zip(startPos, diff))]
pipe = pipeArray[pipePos[0]][pipePos[1]]
areaArray[pipePos[0]][pipePos[1]] = 'X'

while pipe!='S':
    newDiff = pipeDict[(pipe, diff[0], diff[1])]
    if pipe in 'LFJ7':
        clockwiseCheck += clockwise_check(diff, newDiff)
    
    pathList.append([newDiff, diff, pipePos, pipe])
    pipePos = [pipePos[0] + newDiff[0], pipePos[1] + newDiff[1]]
    pipe = pipeArray[pipePos[0]][pipePos[1]]
    areaArray[pipePos[0]][pipePos[1]] = 'X'
    diff = newDiff
    pathLength += 1
    
endTime1 = timer()

print(int(pathLength/2))
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II
startTime2 = timer()

sum2 = 0
diff = 0, 1

for direction, prevDirection, pos, pipe in pathList:
    CWcheck = clockwise_check(prevDirection, direction)

    if pipe=='|':
        checkTiles = [(pos[0], pos[1] + direction[0])]
    elif pipe=='-':
        checkTiles = [(pos[0] - direction[0], pos[1])]
    elif pipe=='J' and CWcheck==1:
        checkTiles = [(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1)]
    elif pipe=='F' and CWcheck==1:
        checkTiles = [(pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)]
    elif pipe=='7' and CWcheck==1:
        checkTiles = [(pos[0] - 1, pos[1]), (pos[0], pos[1] + 1)]
    elif pipe=='L' and CWcheck==1:
        checkTiles = [(pos[0] + 1, pos[1]), (pos[0], pos[1] - 1)]

    for checkTile in checkTiles:
        areaArray = flood_fill(checkTile, areaArray)

for row in areaArray:
    sum2 += row.count('O')

endTime2 = timer()

print(sum2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))