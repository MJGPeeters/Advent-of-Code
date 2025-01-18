from timeit import default_timer as timer

startTime1 = timer()

def replace_index(string, index, replacement):
    """
    Replace text in string starting at given index
 
    Inputs:
    string - String
    index - Integer
    replacement - String

    Outputs:
    string
    """
    return f'{string[:index]}{replacement}{string[index+len(replacement):]}'


def count_arrangements(springs, groups):
    """
    Count possible arrangements for a given arrangement of springs and groups

    Inputs:
    springs - List of groups of '?' and '#' ['??##', '#??#', ...]
    groups - List of integers [2, 3, ...]

    Outputs:
    Integer - Number of possible arrangements
    """

    numArrangements = 0

    fills = ['#'*n for n in groups]

    lenFills = [len(fill) for fill in fills]

    tmpSprings = springs[:]

    tmpSpringNum = 0
    tmpIndex = 0

    for fill, lenFill in zip(fills, lenFills):
        tmpSprings[tmpSpringNum] = replace_index(tmpSprings[tmpSpringNum], tmpIndex, fill)
        tmpIndex += lenFills


    if sum([spring.count('#') for spring in tmpSprings])==sum(groups):
        numArrangements += 1
    
    return numArrangements







    # Place all groups in the first available position
    # Check if it fits

    # Place all but last group in the first available positions
    # Move last group from first to last available position, check if it all works

    # Place all but last two groups in the first available positions
    # Move second to last group one space

    # Move recursively this way, until the first instance of a level does not work anymore
    # For example: group 1 in first position, group 2 moved one right, group 3 and 4 in first positions

    # Keep track of possible arrangements






testName = 'Tests/Test_2023_12.txt'
inputName = 'Inputs/Input_2023_12.txt'

with open(testName, "r") as file:
    fileLines = file.read().splitlines()

ans1 = 0

for line in fileLines:
    springs, groups = line.split()

    springs = list(filter(None, springs.split('.')))
    groups = [n for n in map(int, groups.split(','))]

    # Check if all damaged springs are already accounted for
    if sum([spring.count('#') for spring in springs])==sum(groups):
        ans1 += 1
        continue

    # Remove impossible-to-fill or already filled parts of springs (and of groups for already filled)
    while len(springs[0])<=groups[0]:
        del springs[0]
        if len(springs[0])==groups[0]:
            del groups[0]
    while len(springs[-1])<=groups[-1]:
        del springs[-1]
        if len(springs[-1])==groups[-1]:
            del groups[-1]

    ans1 += count_arrangements(springs, groups)





ans1 = 0

# Special cases:
# n spaces for group of m: n - m + 1 options
# 

endTime1 = timer()

print(ans1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

# startTime2 = timer()

# numCards = [1]*len(fileLines)
# ans2 = 0



# endTime2 = timer()

# print(ans2)
# print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))