from timeit import default_timer as timer
from functools import reduce
import operator

start_time = timer()

DAY_NUMBER = 6
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    homework = [line[0:-1] for line in file]

num_problems, group_size = len(homework[0]), len(homework)-1
grand_total_p1, grand_total_p2 = 0, 0

op_idx_list = [i for i,n in enumerate(homework[group_size]) if n=='+' or n=='*']

for i, op_idx in enumerate(op_idx_list):

    # Determine horizontal numbers and operator
    op = homework[group_size][op_idx]

    # Determine amount of vertical numbers
    if i==len(op_idx_list)-1:
        num_vertical_numbers = len(homework[0]) - op_idx
    else:
        num_vertical_numbers = op_idx_list[i+1] - op_idx_list[i] - 1

    # # Part 1
    nums = [int(homework[r][op_idx:op_idx+num_vertical_numbers]) for r in range(group_size)]
    if op=='+':
        grand_total_p1 += sum(int(nums[j]) for j in range(group_size))
    else:
        grand_total_p1 += reduce(operator.mul, (int(nums[j]) for j in range(group_size)))

    # Part 2
    # Determine the vertical numbers, and either add or multiply them
    nums = []
    for c in range(op_idx, op_idx+num_vertical_numbers):
        num, mult = 0, 1
        for r in range(group_size-1, -1, -1):
            if homework[r][c]!=' ':
                num += int(homework[r][c])*mult
                mult = 10*mult
        nums.append(num)

    if op=='+':
        grand_total_p2 += sum(int(nums[j]) for j in range(num_vertical_numbers))
    else:
        grand_total_p2 += reduce(operator.mul, (int(nums[j]) for j in range(num_vertical_numbers)))

end_time = timer()

print(grand_total_p1)
print(grand_total_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
