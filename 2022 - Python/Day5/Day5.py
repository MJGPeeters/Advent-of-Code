from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 5
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

def move_crate(origin_column, goal_column, crate_stack):
    crate = crate_stack[origin_column-1].pop()
    crate_stack[goal_column-1].append(crate)

    return crate_stack

stacks_status = 1
crate_stack = []
move_array = []
index_list = []

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

## Create array (or heap, or something) of crates
# Find total number of crate stacks
num_crate_columns = int(crate_stack[-1].strip()[-1])
crate_stack_array = [[] for _ in range(num_crate_columns)]

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
            crate_stack_array[i].append(crate)

## Go through all moves of crates
for move_number, move_from, move_to in move_array:
     for _ in range(move_number):
        crate_stack_array = move_crate(move_from, move_to, crate_stack_array)

crate_string = ''
for i in range(len(crate_stack_array)):
    crate_string += crate_stack_array[i][-1]
        
end_time_1 = timer()

print(crate_string)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
