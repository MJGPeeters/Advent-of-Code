from timeit import default_timer as timer

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_18.txt'
INPUT_NAME = 'Inputs/Input_2023_18.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

direction_dict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0),
                  '3': (0, 1), '1': (0, -1), '2': (-1, 0), '0': (1, 0)}

row_1, col_1, row_2, col_2 = 0, 0, 0, 0
volume_1, volume_2 = 0, 0
num_blocks_1, num_blocks_2 = 0, 0

dirs = ['U', 'L', 'D', 'R']
for idx, line in enumerate(file_lines):
    direction_1, number_1, hex_number = line.split()

    # Determine direction and amount of steps for part I
    number_1 = int(number_1)
    d_row_1, d_col_1 = direction_dict[direction_1]
    new_row_1, new_col_1 = row_1 + d_row_1*number_1, col_1 + d_col_1*number_1

    volume_1 += row_1*new_col_1 - col_1*new_row_1
    row_1, col_1 = new_row_1, new_col_1
    num_blocks_1 += number_1

    # Determine direction and amount of steps for part II
    number_2 = int(hex_number[2:-2], 16)
    d_row_2, d_col_2 = direction_dict[hex_number[-2]]
    new_row_2, new_col_2 = row_2 + d_row_2*number_2, col_2 + d_col_2*number_2

    volume_2 += row_2*new_col_2 - col_2*new_row_2
    row_2, col_2 = new_row_2, new_col_2
    num_blocks_2 += number_2

volume_1 = abs(volume_1 / 2) + num_blocks_1 / 2 + 1
volume_2 = abs(volume_2 / 2) + num_blocks_2 / 2 + 1

end_time_1 = timer()

print(int(volume_1))
print(int(volume_2))
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
