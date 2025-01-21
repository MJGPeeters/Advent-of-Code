from timeit import default_timer as timer
import numpy as np

startTime1 = timer()

TEST_NAME = 'Tests/Test_2023_14.txt'
INPUT_NAME = 'Inputs/Input_2023_14.txt'

with open(TEST_NAME, "r") as file:
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

# # Part II

startTime2 = timer()

ans2 = 0

def tilt_cycle_platform(platform):
    """
    Determine location of 'O' after tilting platform for one cycle

    Inputs:
    platform - List of lists with '.' empty space, '#' stationary stones, 'O' rolling stones

    Notes:
    On first go stones roll to the right, make sure platform is input correctly
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
                # elif thing=='.':
                #     continue

            platform[start_index:start_index + round_stones, col_num] = 'O'
            platform[start_index + round_stones:len(col), col_num] = '.'
        num_tilts += 1

    return platform

# Rotate back once, so that it goes into the module right the first time
rock_platform = np.rot90(platform, k=1)

num_cycles = 10000

for i in range(num_cycles):
    rock_platform_new = np.array(rock_platform)

    rock_platform_new = np.rot90(rock_platform_new, k=1)
    rock_platform_new = tilt_cycle_platform(rock_platform_new)
    rock_platform_new = np.rot90(rock_platform_new, k=1, axes=(1, 0))

    if (rock_platform_new==rock_platform).all():
        print(i)
        break
    rock_platform = np.array(rock_platform_new)

# rock_platform = np.rot90(rock_platform, k=1, axes=(1, 0))

endTime2 = timer()

print(ans2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
