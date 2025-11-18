from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 5
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

def move_crate_9000(origin_column, goal_column, crate_stack):
    crate = crate_stack[origin_column-1].pop()
    crate_stack[goal_column-1].append(crate)

    return crate_stack

def move_crate_9001(origin_column, goal_column, crate_number, crate_stack):
    crates = []
    for _ in range(crate_number):
        crate = crate_stack[origin_column-1].pop()
        crates.append(crate)
    
    for _ in range(crate_number):
        crate = crates.pop()
        crate_stack[goal_column-1].append(crate)

    return crate_stack

crate_stack, move_array, index_list = [], [], []
crate_string_9000, crate_string_9001 = '', ''

stacks_status = 1
with open(FILE_NAME, 'r') as file:
    for line in file:
        if line=='\n':
            stacks_status = 0
            continue

        if stacks_status:
            crate_stack.append(line)
        else:
            moves = line.split()
            move_array.append([int(moves[1]), int(moves[3]), int(moves[5])])

## Create list of crates
# Find total number of crate stacks
num_crate_columns = int(crate_stack[-1].strip()[-1])
crate_stack_array_9000 = [[] for _ in range(num_crate_columns)]
crate_stack_array_9001 = [[] for _ in range(num_crate_columns)]

# Find indices for all columns
for i in range(num_crate_columns):
    column_index = crate_stack[-1].index(str(i+1))
    index_list.append(column_index)

# Fill arrays with correct boxes
for i, index in enumerate(index_list):
    for line_number in range(len(crate_stack[0:-2]),-1,-1):
        line = crate_stack[line_number]
        crate = line[index]
        if crate != ' ':
            crate_stack_array_9000[i].append(crate)
            crate_stack_array_9001[i].append(crate)

## Go through all moves of crates
# Part 1 - Crate Mover 9000
for move_number, move_from, move_to in move_array:
     for _ in range(move_number):
        crate_stack_array = move_crate_9000(move_from, move_to, crate_stack_array_9000)

for i in range(len(crate_stack_array_9000)):
    crate_string_9000 += crate_stack_array_9000[i][-1]

# Part 2 - Crate Mover 9001
for move_number, move_from, move_to in move_array:
    crate_stack_array = move_crate_9001(move_from, move_to, move_number, crate_stack_array_9001)

for i in range(len(crate_stack_array_9001)):
    crate_string_9001 += crate_stack_array_9001[i][-1]

end_time_1 = timer()

print(crate_string_9000)
print(crate_string_9001)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
