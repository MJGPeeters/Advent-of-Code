from timeit import default_timer as timer

def tilt_platform_north(platform):
    """
    Determine location of 'O' after tilting platform north
    """

    PLATFORM_SIZE = len(platform)

    for i_col in range(PLATFORM_SIZE):
        i_empty = 0

        for i_row in range(PLATFORM_SIZE):
            thing = platform[i_row][i_col]
            if thing=='O':
                platform[i_row][i_col] = '.'
                platform[i_empty][i_col] = 'O'
                i_empty += 1
            elif thing=='#':
                i_empty = i_row + 1

    return platform

def tilt_platform_south(platform):
    """
    Determine location of 'O' after tilting platform south
    """

    PLATFORM_SIZE = len(platform)

    for i_col in range(PLATFORM_SIZE):
        i_empty = PLATFORM_SIZE - 1

        for i_row in reversed(range(PLATFORM_SIZE)):
            thing = platform[i_row][i_col]
            if thing=='O':
                platform[i_row][i_col] = '.'
                platform[i_empty][i_col] = 'O'
                i_empty -= 1
            elif thing=='#':
                i_empty = i_row - 1

    return platform

def tilt_platform_west(platform):
    """
    Determine location of 'O' after tilting platform west
    """

    for i_row, row in enumerate(platform):
        i_empty = 0

        for i_col, thing in enumerate(row):
            if thing=='O':
                platform[i_row][i_col] = '.'
                platform[i_row][i_empty] = 'O'
                i_empty += 1
            elif thing=='#':
                i_empty = i_col + 1

    return platform

def tilt_platform_east(platform):
    """
    Determine location of 'O' after tilting platform east and calculate load on north beams
    """

    PLATFORM_SIZE = len(platform)
    load = 0

    for i_row, row in enumerate(platform):
        i_empty = PLATFORM_SIZE - 1

        for i_col, thing in reversed(list(enumerate(row))):
            if thing=='O':
                platform[i_row][i_col] = '.'
                platform[i_row][i_empty] = 'O'
                i_empty -= 1
                load += PLATFORM_SIZE - i_row
            elif thing=='#':
                i_empty = i_col - 1

    return platform, load

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_14.txt'
INPUT_NAME = 'Inputs/Input_2023_14.txt'

with open(INPUT_NAME, "r") as file:
    file_lines = file.read().splitlines()

ans1 = 0

platform = []

for line in file_lines:
    platform.append(list(line))

PLATFORM_SIZE = len(platform)

for i_col in range(PLATFORM_SIZE):
    i_empty = 0

    for i_row in range(PLATFORM_SIZE):
        thing = platform[i_row][i_col]
        if thing=='O':
            platform[i_row][i_col] = '.'
            platform[i_empty][i_col] = 'O'
            ans1 += PLATFORM_SIZE - i_empty
            i_empty += 1
        elif thing=='#':
            i_empty = i_row + 1

end_time_1 = timer()

print(int(ans1))
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# Part II

startTime2 = timer()

previous_platforms, previous_loads = {}, []
cycle_num = 0

while True:
    platform = tilt_platform_north(platform)
    platform = tilt_platform_west(platform)
    platform = tilt_platform_south(platform)
    platform, load = tilt_platform_east(platform)

    platform_tuple = tuple(tuple(row) for row in platform)

    if platform_tuple in previous_platforms:
        prev_cycle_num = previous_platforms[platform_tuple]
        break

    previous_platforms[platform_tuple] = cycle_num
    previous_loads.append(load)
    cycle_num += 1

cycle_length = cycle_num - prev_cycle_num
offset = prev_cycle_num % cycle_length
cycle_index = (10**9 - offset) % cycle_length + prev_cycle_num - 1

ans2 = previous_loads[cycle_index]

endTime2 = timer()

print(ans2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
