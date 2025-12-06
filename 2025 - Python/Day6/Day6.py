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
    homework = [line.strip().split() for line in file]

num_problems, group_size = len(homework[0]), len(homework)-1
grand_total = 0

for i in range(num_problems):
    if homework[group_size][i]=='+':
        grand_total += sum(int(homework[j][i]) for j in range(group_size))
    else:
        grand_total += reduce(operator.mul, (int(homework[j][i]) for j in range(group_size)))

end_time = timer()

print(grand_total)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
