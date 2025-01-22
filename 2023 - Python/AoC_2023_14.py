from timeit import default_timer as timer

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

def tilt_cycle_platform(platform):
    """
    Determine location of 'O' after tilting platform north
    """

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
