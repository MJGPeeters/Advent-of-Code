from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 7
TEST = True

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    terminal_output = [line.strip() for line in file]

size_sum = 0

end_time_1 = timer()

print(size_sum)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
