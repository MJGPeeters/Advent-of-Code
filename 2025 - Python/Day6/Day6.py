from timeit import default_timer as timer
from functools import reduce
import operator

def add_or_multiply(numbers, op):
    if op=='+':
        return sum(number for number in numbers)
    else:
        return reduce(operator.mul, (number for number in numbers))

start_time = timer()

DAY_NUMBER = 6
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    homework = [line[0:-1] for line in file]

group_rows = len(homework)-1
grand_total_p1, grand_total_p2 = 0, 0

op_idx_list = [i for i,n in enumerate(homework[group_rows]) if n=='+' or n=='*']

for op_num, op_idx in enumerate(op_idx_list):
    op = homework[group_rows][op_idx]

    if op_num==len(op_idx_list)-1:
        group_cols = len(homework[0]) - op_idx
    else:
        group_cols = op_idx_list[op_num+1] - op_idx_list[op_num] - 1

    numbers_1 = [int(homework[r][op_idx:op_idx+group_cols]) for r in range(group_rows)]

    numbers_2 = []
    for c in range(op_idx, op_idx+group_cols):
        num, mult = 0, 1
        for r in range(group_rows-1, -1, -1):
            if homework[r][c]!=' ':
                num += int(homework[r][c])*mult
                mult = 10*mult
        numbers_2.append(num)

    grand_total_p1 += add_or_multiply(numbers_1, op)
    grand_total_p2 += add_or_multiply(numbers_2, op)

end_time = timer()

print(grand_total_p1)
print(grand_total_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
