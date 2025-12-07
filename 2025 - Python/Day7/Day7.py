from timeit import default_timer as timer

def num_timelines(splitter, splitter_dict):
    if splitter in splitter_dict:
        return splitter_dict[splitter], splitter_dict

    timelines = 0

    for side in (-1, 1):
        new_splitter = ()
        new_col = splitter[1] + side

        for i in range(splitter[0]+2, diagram_height, 2):
            if (i,new_col) in splitters:
                new_splitter = (i,new_col)
                break

        if not new_splitter:
            timelines += 1
        else:
            timelines += num_timelines(new_splitter, splitter_dict)[0]

    splitter_dict[splitter] = timelines

    return timelines, splitter_dict

start_time = timer()

DAY_NUMBER = 7
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    manifold_diagram = [line.strip() for line in file]

diagram_height = len(manifold_diagram)
splitters = set()
splitter_dict = {}

for row_num, row in enumerate(manifold_diagram):
    if row_num==0:
        initial_col = row.find('S')
    elif row_num%2==0:
        splitters.update((row_num,col_num) for col_num, x in enumerate(row) if x=='^')

total_timelines, splitter_dict = num_timelines((2,initial_col), {})
total_splits = len(splitter_dict)

end_time = timer()

print(total_splits)
print(total_timelines)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
