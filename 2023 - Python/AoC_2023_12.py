from timeit import default_timer as timer

startTime1 = timer()

def count_arrangements(springs, groups):
    """
    Count possible arrangements for a given arrangement of springs and groups

    Inputs:
    springs - List of groups of '?#' ['??##', '#??#', ...]
    groups - List of integers [2, 3, ...]

    Outputs:
    Integer - Number of possible arrangements
    """

    

testName = 'Tests/Test_2023_12.txt'
inputName = 'Inputs/Input_2023_12.txt'

with open(inputName, "r") as file:
    fileLines = file.read().splitlines()

for line in fileLines:
    springs, groups = line.split()

    springs = list(filter(None, springs.split('.')))
    groups = groups.split(',')

    while len(springs[0]) < int(groups[0]):
        del springs[0]
    
    while len(springs[-1]) < int(groups[-1]):
        del springs[-1]

    if len(springs[0]) < (int(groups[0]) + 1 + int(groups[1])):
        count_arrangements(springs[0], groups[0])
        count_arrangements(springs[1:], groups[1:])
    elif len(springs[-1]) < (int(groups[-1]) + 1 + int(groups[-2])):
        count_arrangements(springs[-1], groups[-1])
        count_arrangements(springs[:-2], groups[:-2])

    x = 1





ans1 = 0

# Split into blocks at '.'

# For every block, find maximum number of groups that fit into it (e.g. size 5 can fit 1,1,1 as #.#.#)

# From the left and right, see if blocks can be thrown away (e.g. for size 2 block when groups start with 5)

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