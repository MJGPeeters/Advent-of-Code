from timeit import default_timer as timer

def find_directory_size(directory_name):
    directory_size = 0

    for element in file_system[directory_name]:
        if isinstance(element, int):
            directory_size += element
        else:
            directory_size += find_directory_size(element)

    return directory_size

start_time_1 = timer()

DAY_NUMBER = 7
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    terminal_output = [line.strip() for line in file]

file_system = {'/': []}
current_dir = '/'
size_sum = 0

## Go through terminal output and find relevant groups of output
for line in terminal_output:
    if line=='$ cd /' or line=='$ cd ..' or line=='$ ls':
        continue

    if line[0]=='d':
        file_system[current_dir].append(line[4:])
    
    elif line[0] in '0123456789':
        file_system[current_dir].append(int(line.split()[0]))

    else:
        current_dir = line[5:]
        file_system[current_dir] = []

size_sum = 0

## Go through file_system and find sizes of all directories
for dir in file_system:
    dir_size = find_directory_size(dir)
    if dir_size <= 100000:
        size_sum += dir_size

end_time_1 = timer()

print(size_sum)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
