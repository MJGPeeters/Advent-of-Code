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
    if line=='$ cd /' or line=='$ ls':
        continue

    elif line=='$ cd ..':
        tmp_index = current_dir[0:-1].rfind('/')
        current_dir = current_dir[0:tmp_index] + '/'

    elif line[0]=='d':
        file_system[current_dir].append(current_dir + line[4:] + '/')
    
    elif line[0] in '0123456789':
        file_system[current_dir].append(int(line.split()[0]))

    else:
        current_dir = current_dir + line[5:] + '/'
        file_system[current_dir] = []

size_sum = 0

TOTAL_DISK_SPACE = 70000000
TOTAL_REQUIRED_SPACE = 30000000

USED_SPACE = find_directory_size('/')
EMPTY_SPACE = TOTAL_DISK_SPACE - USED_SPACE

MIN_DIR_SIZE = TOTAL_REQUIRED_SPACE - EMPTY_SPACE

smallest_dir_size = TOTAL_DISK_SPACE

## Go through file_system and find sizes of all directories
for dir in file_system:
    dir_size = find_directory_size(dir)

    if dir_size <= 100000:
        size_sum += dir_size

    if dir_size>=MIN_DIR_SIZE and dir_size<smallest_dir_size:
        smallest_dir_size = dir_size

end_time_1 = timer()

print(size_sum)
print(smallest_dir_size)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
