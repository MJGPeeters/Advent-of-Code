from timeit import default_timer as timer

def range_to_new_ranges(plan, range):
    """ Converts source range to destination range(s)

    Inputs
    plan - list of lists [[source_begin, source_end, diff], ...]
    range - tuple (begin, end)

    Outputs
    newRanges - list of tuples [(begin, end), (begin, end), ...]
    """

    rangeStart = -1
    sourceRanges = []

    # Generate scopes from plan
    scopes = [x for scope in plan for x in (scope[0], scope[1])]

    # Insert source range in list of destination ranges
    scopes.extend([range[0], range[1]])
    tmpScopes = sorted(scopes)

    # Use only the part that is in the source range
    tmpScopes = tmpScopes[tmpScopes.index(range[0]):tmpScopes.index(range[1])+1]

    # Generate new ranges
    for rangeEnd in tmpScopes:
        if rangeStart==-1:
            rangeStart = rangeEnd
        elif rangeStart!=rangeEnd:
            sourceRanges.append((rangeStart, rangeEnd))
            rangeStart = rangeEnd

    # Apply rules to sourceRanges
    newRanges = [(dest_pos(x, plan), dest_pos(y, plan)) for x, y in sourceRanges]

    return newRanges

def dest_pos(sourcePos, plan):
    """ Converts source position to destination position

    Inputs
    sourcePos - int
    plan - list of lists list of lists [[source_begin, source_end, diff], ...]

    Outputs
    destPos - int
    """

    destPos = sourcePos

    for scope in plan:
        if scope[0]<=sourcePos<scope[1]:
            destPos += scope[2]
            break

    return destPos

# Part I
startTime1 = timer()

testName = 'Tests/Test_2023_5.txt'
inputName = 'Inputs/Input_2023_5.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

plans = []
seedRanges = []
planIdx = -1

# Make list of seeds and arrays for the different plans, in the format [source_begin, source_end, diff]
for line in fileLines:
    sLine = line.split()
    if sLine==[]:
        plans.append([])
        planIdx += 1
    elif sLine[0]=='seeds:':
        seeds = [int(seed) for seed in sLine if seed.isdigit()]
        for i, x in enumerate(seeds):
            if i%2==0:
                tmp = x
            else:
                seedRanges.append((tmp, x + tmp))
    elif sLine[0].isdigit():
        x = [int(sLine[1]), int(sLine[1]) + int(sLine[2]), int(sLine[0]) - int(sLine[1])]
        plans[planIdx].append(x)
 
minLocation = 10**10

for seed in seeds:
    number = seed
    for plan in plans:
        number = dest_pos(number, plan)
    
    if number<minLocation:
        minLocation = number

endTime1 = timer()

print(minLocation)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II
startTime2 = timer()

# Destination ranges and source range
scopes = [5, 14, 23, 31]
range = (12, 26)

sourceRanges = seedRanges

for plan in plans:
    destRanges = []

    for sourceRange in sourceRanges:
        tmp = range_to_new_ranges(plan, sourceRange)
        for tmpRange in tmp:
            destRanges.append(tmpRange)
    
    sourceRanges = destRanges
    
minRange = 10**10

for startRange, endRange in destRanges:
    if startRange<minRange:
        minRange = startRange

endTime2 = timer()

print(minRange)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))