from timeit import default_timer as timer
from collections import deque as dq

def start_machine(goal, steps):
    starting_point = tuple(0 for _ in range(len(goal)))

    visited_points = {starting_point:0}
    queue = dq([starting_point])

    while queue:
        current_point = queue.popleft()
        current_presses = visited_points[current_point]

        if current_point==goal:
            return visited_points[goal]
        
        for step in steps:
            new_point = tuple(sum(x)%2 for x in zip(current_point,step))
            if new_point not in visited_points:
                visited_points[new_point] = current_presses + 1
                queue.append(new_point)

start_time = timer()

DAY_NUMBER = 10
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

manual = []

with open(FILE_NAME, 'r') as file:
    for line in file:
        tmp = line.strip().split()

        goal = tuple(1 if x=='#' else 0 for x in tmp[0][1:-1])
        
        schematics = []
        for schematic in tmp[1:-1]:
            steps = {int(b) for b in schematic[1:-1].split(',')}
            schematics.append(tuple(1 if x in steps else 0 for x in range(len(goal))))

        joltages = tuple(int(j) for j in tmp[-1][1:-1].split(','))

        manual.append([goal, schematics, joltages])

total_presses = 0

for machine in manual:
    goal, steps, joltages = machine

    total_presses += start_machine(goal, steps)

end_time = timer()

print(total_presses)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
