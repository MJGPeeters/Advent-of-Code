from timeit import default_timer as timer
import numpy as np

def load_calculation(platform):
    """
    Calculate load on north support beams
    """

    total_load = 0

    for col in platform.T:
        load = 0
        round_stones = 0
        max_index = len(col)

        for i, thing in enumerate(col):
            if thing=='O':
                load += max_index - i

        total_load += load
    
    return total_load

startTime1 = timer()

TEST_NAME = 'Tests/Test_2023_14.txt'
INPUT_NAME = 'Inputs/Input_2023_14.txt'

with open(INPUT_NAME, "r") as file:
    file_lines = file.read().splitlines()

ans1 = 0

platform = []

for line in file_lines:
    platform.append(list(line))

platform = np.array(platform)

for col in platform.T:
    load = 0
    round_stones = 0
    start_index = len(col)

    for i, thing in enumerate(col):
        if thing=='O':
            round_stones += 1
        elif thing=='#':
            load += round_stones * (start_index - (round_stones - 1) / 2)
            start_index = len(col) - i - 1
            round_stones = 0

    load += round_stones * (start_index - (round_stones - 1) / 2)

    ans1 += load
    
endTime1 = timer()

print(int(ans1))
print(f'Time elapsed: {endTime1 - startTime1:.6f} s')

# Part II

startTime2 = timer()

def tilt_cycle_platform(platform):
    """
    Determine location of 'O' after tilting platform for one cycle

    Inputs:
    platform - List of lists with '.' empty space, '#' stationary stones, 'O' rolling stones

    Notes:
    Make sure platform rotation in input  is correct
    """

    num_tilts = 0

    while num_tilts<4:
        # Rotate platform
        platform = np.rot90(platform, k=1, axes=(1, 0))

        # Go through the platform column by column, move everything to the top
        for col_num, col in enumerate(platform.T):
            round_stones = 0
            start_index = 0

            for i, thing in enumerate(col):
                if thing=='O':
                    round_stones += 1
                elif thing=='#':
                    # MOVE STONES
                    platform[start_index:start_index + round_stones, col_num] = 'O'
                    platform[start_index + round_stones:i, col_num] = '.'
                    start_index = i + 1
                    round_stones = 0

            platform[start_index:start_index + round_stones, col_num] = 'O'
            platform[start_index + round_stones:len(col), col_num] = '.'
        num_tilts += 1

    return platform

rock_platform = platform

num_cycles = 130
load_list = []

for i in range(num_cycles):
    rock_platform_new = np.array(rock_platform)

    rock_platform_new = np.rot90(rock_platform_new, k=1)
    rock_platform_new = tilt_cycle_platform(rock_platform_new)
    rock_platform_new = np.rot90(rock_platform_new, k=1, axes=(1, 0))

    rock_platform = np.array(rock_platform_new)

    load_list.append(load_calculation(rock_platform))


check_length = 10
break_flag = 0

for start_idx in range(num_cycles):
    test_pattern = load_list[start_idx:start_idx+check_length]

    for idx in range(start_idx + 1, num_cycles):
        if load_list[idx]==test_pattern[0] and load_list[idx:idx+check_length]==test_pattern:
            loop_starts = [start_idx, idx]
            break_flag = 1
            break
    if break_flag:
        break

cycle_length = loop_starts[1] - loop_starts[0]
offset = loop_starts[0] % cycle_length
cycle_index = (10**9 - offset) % cycle_length + loop_starts[0] - 1

ans2 = load_list[cycle_index]

endTime2 = timer()

print(ans2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
