from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_16.txt'
inputName = 'Inputs/Input_2023_16.txt'

with open(testName, "r") as file:
    fileLines = file.read().splitlines()

layout, tiles = [], []

for line in fileLines:
    layout.append([c for c in line])
    tiles.append(['.' for c in line])

def energized_tiles(layout, tiles, location, direction):
    """
    Determine energized tiles for a light beam coming in with direction at location
    """

    limit = len(tiles) - 1

    row, col = location
    tiles[row][col] = '#'

    row, col = row + direction[0], col + direction[1]
    if not (0<=row<=limit and 0<=col<=limit):
        return tiles
    
    tiles[row][col] = '#'    

    while layout[row][col]=='.':
        row, col = row + direction[0], col + direction[1]
        if not (0<=row<=limit and 0<=col<=limit):
            return tiles
        
        tiles[row][col] = '#'
    
    if layout[row][col]=='/':
        directions = [(-direction[1], -direction[0])]
    elif layout[row][col]=='\\':
        directions = [(direction[1], direction[0])]
    elif layout[row][col]=='-' and direction[0]==0:
        directions = [direction]
    elif layout[row][col]=='-':
        directions = [(0, 1), (0, -1)]
    elif layout[row][col]=='|' and direction[1]==0:
        directions = [direction]
    elif layout[row][col]=='|':
        directions = [(1, 0), (-1, 0)]

    for direction in directions:
        tiles = energized_tiles(layout, tiles, (row, col), direction)

    return tiles

ans1 = 0

tiles = energized_tiles(layout, tiles, (0, 0), (0, 1))

endTime1 = timer()

print(ans1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# # Part II

# startTime2 = timer()

# ans2 = 0



# endTime2 = timer()

# print(ans2)
# print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
