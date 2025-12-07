from timeit import default_timer as timer

def num_timelines(splitter_set, diagram_height, splitter, mem_dict):
    if splitter in mem_dict:
        return mem_dict[splitter]
    else:
        timelines = 0
    
    # Determine new paths (splitter-1, splitter+1)
    splitter_row, splitter_col = splitter
    left_col = splitter_col - 1
    right_col = splitter_col + 1

    # Find next splitter on each path
    left_splitter, right_splitter = (), ()
    
    for i in range(splitter_row+2, diagram_height, 2):
        if (i,left_col) in splitter_set:
            left_splitter = (i,left_col)
            break

    for i in range(splitter_row+2, diagram_height, 2):
        if (i,right_col) in splitter_set:
            right_splitter = (i,right_col)
            break        

    # If there is no next splitter, this counts as one extra timeline,
    # if there is a next splitter, add num_timelines(splitter_set, NEW_splitter)
    if not left_splitter:
        timelines += 1
    else:
        timelines += num_timelines(splitter_set, diagram_height, left_splitter, mem_dict)

    if not right_splitter:
        timelines += 1
    else:
        timelines += num_timelines(splitter_set, diagram_height, right_splitter, mem_dict)

    mem_dict[splitter] = timelines

    return timelines

    # Use memoization to store the total amount of timelines after a certain splitter once it's known

start_time = timer()

DAY_NUMBER = 7
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

# split_count = 0

# for line_number, line in enumerate(open(FILE_NAME, 'r')):
#     if line_number==0:
#         tachyons = {line.find('S')}
#         continue
#     elif line_number%2==1:
#         continue

#     splitters = (idx for idx, x in enumerate(line) if x=='^')

#     for splitter in splitters:
#         if splitter in tachyons:
#             tachyons.remove(splitter)
#             tachyons.add(splitter-1)
#             tachyons.add(splitter+1)
#             split_count += 1

with open(FILE_NAME, 'r') as file:
    manifold_diagram = [line.strip() for line in file]

splitters = set()
mem_dict = {}

for row_num, row in enumerate(manifold_diagram):
    if row_num==0:
        initial_col = row.find('S')
    elif row_num%2==0:
        splitters.update((row_num,col_num) for col_num, x in enumerate(row) if x=='^')

timelines = num_timelines(splitters, len(manifold_diagram), (2,initial_col), {})

end_time = timer()

print(timelines)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
