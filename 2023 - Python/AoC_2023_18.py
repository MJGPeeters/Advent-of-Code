from timeit import default_timer as timer

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_18.txt'
INPUT_NAME = 'Inputs/Input_2023_18.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

# layout_size = 500
# layout = [['.' for _ in range(layout_size)] for _ in range(layout_size)]

map_dict = {}
direction_dict = {
    'U': (-1, 0),
    'D': (+1, 0),
    'L': (0, +1),
    'R': (0, -1)
}

row, col = 0, 0 #int(layout_size/2) + 180, int(layout_size/2)

min_row, max_row = 999, 0
min_col, max_col = 999, 0

for line in file_lines:
    direction, number, _ = line.split()
    
    number = int(number)
    row_diff, col_diff = direction_dict[direction]

    tmp_row = row + row_diff*number
    min_row = tmp_row if tmp_row < min_row else min_row
    max_row = tmp_row if tmp_row > max_row else max_row
    tmp_col = col + col_diff*number
    min_col = tmp_col if tmp_col < min_col else min_col
    max_col = tmp_col if tmp_col > max_col else max_col

    for i in range(number):
        row, col = row + row_diff, col + col_diff
        map_dict[(row, col)] = None

 # IMPLEMENT FLOOD FILL
volume = 0

# volume = sum(1 for col in range(min_col, max_col+1) if (min_row, col) in map_dict)

# for i in range(min_row+1, max_row):
#     wall_flag = 0
#     in_flag = -1

#     for j in range(min_col, max_col+1):
#         if (i, j) in map_dict:
#             wall_flag = 1
#         elif wall_flag==1:
#             in_flag = in_flag * -1
#             wall_flag = 0
        
#         if wall_flag==1 or in_flag==1:
#             volume += 1

# volume += sum(1 for col in range(min_col, max_col+1) if (max_row, col) in map_dict)

end_time_1 = timer()

print(volume)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# # Part II

# start_time_2 = timer()

# ans2 = 0



# end_time_2 = timer()

# print(ans2)
# print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')