from timeit import default_timer as timer

def flood_fill(point, filled_set):
    """
    Fill the whole area enclosed by the borders in array, with point in it

    Inputs:
    point - tuple with grid coordinates (row, column)
    filled - set with squares as entries, anything else as not entries

    Outputs:
    set with filled squares as entries, anything else as not entries
    """

    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    row, col = point

    # Includes all points in the area, for which neighbors are not yet checked
    point_set = {point}

    filled_set.add(point)

    # Continue with loop until point_set is empty (all neighbors are checked)
    while point_set:
        tmp_row, tmp_col = point_set.pop()

        # Check all four neighbors, add them to filled, update point_set
        for row_diff, col_diff in neighbors:
            check_point = tmp_row + row_diff, tmp_col + col_diff
            if check_point not in filled_set:
                filled_set.add(check_point)
                point_set.add(check_point)
    
    return filled_set

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_18.txt'
INPUT_NAME = 'Inputs/Input_2023_18.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

# layout_size = 500
# layout = [['.' for _ in range(layout_size)] for _ in range(layout_size)]

filled = set()
direction_dict = {
    'U': (-1, 0),
    'D': (+1, 0),
    'L': (0, +1),
    'R': (0, -1)
}

row, col = 0, 0

min_row, max_row = 0, 0
min_col, max_col = 0, 0

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
        filled.add((row, col))

filled = flood_fill((0, 0), filled)

end_time_1 = timer()

print(len(filled))
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# Part II

start_time_2 = timer()

ans2 = 0

# New algorithm for parts I and II
# Read in data from file, fill numpy arrays for both part I and part II
# For both numpy arrays, calculate determinant
# Divide by two for answers

end_time_2 = timer()

print(ans2)
print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')