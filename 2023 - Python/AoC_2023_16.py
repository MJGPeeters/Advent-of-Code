from timeit import default_timer as timer

startTime1 = timer()

TEST_NAME = 'Tests/Test_2023_16.txt'
INPUT_NAME = 'Inputs/Input_2023_16.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

layout, tiles = [], []

for line in file_lines:
    layout.append(list(line))
    tiles.append(['.' for _ in line])

def energized_tiles(layout, tiles, location, direction):
    """
    Determine energized tiles for a light beam coming in with direction at location
    """

    MAX_INDEX = len(tiles) - 1

    row, col = location

    # if (row, col, direction) in visited:
    #     return tiles

    # tiles[row][col] = '#'
    # visited.add((row, col, direction))

    row, col = row + direction[0], col + direction[1]
    if (row, col, direction) in visited or not (0<=row<=MAX_INDEX and 0<=col<=MAX_INDEX):
        return tiles

    tiles[row][col] = '#'
    visited.add((row, col, direction))

    while layout[row][col]=='.':
        row, col = row + direction[0], col + direction[1]
        if (row, col, direction) in visited or not (0<=row<=MAX_INDEX and 0<=col<=MAX_INDEX):
            return tiles

        tiles[row][col] = '#'
        visited.add((row, col, direction))

    tile = layout[row][col]

    if tile=='/':
        directions = [(-direction[1], -direction[0])]
    elif tile=='\\':
        directions = [(direction[1], direction[0])]
    elif tile=='-' and direction[0]==0:
        directions = [direction]
    elif tile=='-':
        directions = [(0, 1), (0, -1)]
    elif tile=='|' and direction[1]==0:
        directions = [direction]
    elif tile=='|':
        directions = [(1, 0), (-1, 0)]

    for direction in directions:
        tiles = energized_tiles(layout, tiles, (row, col), direction)

    return tiles

initial_location = (0, -1)
initial_direction = (0, 1)

# tiles[initial_location[0]][initial_location[1]] = '#'
visited = set((initial_location[0], initial_location[1], initial_direction))
tiles = energized_tiles(layout, tiles, initial_location, initial_direction)

ans1 = sum((row.count('#') for row in tiles))

endTime1 = timer()

print(ans1)
print(f'Time elapsed: {endTime1 - startTime1:.6f} s')

# # Part II

# startTime2 = timer()

# ans2 = 0



# endTime2 = timer()

# print(ans2)
# print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
