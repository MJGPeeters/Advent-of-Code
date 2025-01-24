from timeit import default_timer as timer

def energized_tiles(layout, tiles_set, location, direction):
    """
    Determine energized tiles for a light beam coming in with direction at location
    """

    MAX_INDEX = len(layout) - 1

    row, col = location

    row, col = row + direction[0], col + direction[1]
    if (row, col, direction) in visited or not (0<=row<=MAX_INDEX and 0<=col<=MAX_INDEX):
        return tiles_set

    tiles_set.add((row, col))
    visited.add((row, col, direction))

    while layout[row][col]=='.':
        row, col = row + direction[0], col + direction[1]
        if (row, col, direction) in visited or not (0<=row<=MAX_INDEX and 0<=col<=MAX_INDEX):
            return tiles_set

        tiles_set.add((row, col))
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
        tiles_set = energized_tiles(layout, tiles_set, (row, col), direction)

    return tiles_set

startTime1 = timer()

TEST_NAME = 'Tests/Test_2023_16.txt'
INPUT_NAME = 'Inputs/Input_2023_16.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

layout = [[e for e in line] for line in file_lines]

initial_location = (0, -1)
initial_direction = (0, 1)
visited = set((initial_location[0], initial_location[1], initial_direction))

tiles = energized_tiles(layout, set(), initial_location, initial_direction)

ans1 = len(tiles)

endTime1 = timer()

print(ans1)
print(f'Time elapsed: {endTime1 - startTime1:.6f} s')

# Part II

startTime2 = timer()

MAP_SIZE = len(layout)
most_tiles = 0

for i in range(MAP_SIZE):
    # Up
    r_start, c_start = MAP_SIZE, i
    dir_start = (-1, 0)
    visited = {(r_start, c_start, dir_start)}
    tiles = energized_tiles(layout, set(), (r_start, c_start), dir_start)
    num_tiles_up = len(tiles)

    # Down
    r_start, c_start = -1, i
    dir_start = (1, 0)
    visited = {(r_start, c_start, dir_start)}
    tiles = energized_tiles(layout, set(), (r_start, c_start), dir_start)
    num_tiles_down = len(tiles)

    # Left
    r_start, c_start = i, MAP_SIZE
    dir_start = (0, -1)
    visited = {(r_start, c_start, dir_start)}
    tiles = energized_tiles(layout, set(), (r_start, c_start), dir_start)
    num_tiles_left = len(tiles)

    # Right
    r_start, c_start = i, -1
    dir_start = (0, 1)
    visited = {(r_start, c_start, dir_start)}
    tiles = energized_tiles(layout, set(), (r_start, c_start), dir_start)
    num_tiles_right = len(tiles)

    tmp_most_tiles = max(num_tiles_up, num_tiles_down, num_tiles_left, num_tiles_right)

    most_tiles = tmp_most_tiles if tmp_most_tiles>most_tiles else most_tiles

endTime2 = timer()

print(most_tiles)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
