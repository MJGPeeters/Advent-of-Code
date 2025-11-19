from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 7
TEST = True

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

# def make_file_system(input_file_system, contents):


#     return output_file_system

with open(FILE_NAME, 'r') as file:
    terminal_output = [line.strip() for line in file]

FILE_START = '0123456789'
DIR_START = 'd'
file_system = {}
size_sum = 0

## Go through terminal output and find relevant groups of output
for line in terminal_output:
    if line=='$ cd /' or line=='$ ls':
        continue



    if line[0] in FILE_START:
        file_system

    if line[0] in DIR_START:
        file_system

    if line=='$ cd'


end_time_1 = timer()

print(size_sum)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
