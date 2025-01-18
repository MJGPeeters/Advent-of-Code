from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_14.txt'
inputName = 'Inputs/Input_2023_14.txt'

with open(inputName, "r") as file:
    fileLines = file.read().splitlines()

ans1 = 0

platform = []

for line in fileLines:
    platform.append([x for x in line])

platform = list(zip(*platform))

for row in platform:
    load = 0
    roundStones = 0
    startIndex = len(row)

    for i, thing in enumerate(row):
        if thing=='O':
            roundStones += 1
        elif thing=='#':
            load += roundStones * (startIndex - (roundStones - 1) / 2)
            startIndex = len(row) - i - 1
            roundStones = 0
    
    load += roundStones * (startIndex - (roundStones - 1) / 2)

    ans1 += load

endTime1 = timer()

print(int(ans1))
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# # Part II

startTime2 = timer()

ans2 = 0

def tilt_platform(platform, direction):
    """
    Determine location of 'O' after tilting platform in a certain direction

    Inputs:
    platform - np.array with '.' as empty space, '#' as stationary stones, 'O' as rolling stones
    direction - Integer: 0, 1, 2, 3 corresponds to north, east, south, west
    """

    

print(ans2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
