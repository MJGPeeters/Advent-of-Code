from timeit import default_timer as timer
import cmath

start_time_1 = timer()

DAY_NUMBER = 9
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    motions = [line.strip() for line in file]

direction_dict = {'U': 1j, 'D': -1j, 'R':1, 'L':-1}

head_pos, tail_pos = 0, 0
visited_positions = {tail_pos}

for motion in motions:
    direction, amount = motion.split()

    for i in range(int(amount)):
        head_pos += direction_dict[direction]

        if abs(tail_pos.real-head_pos.real)>1 or abs(tail_pos.imag-head_pos.imag)>1:
            tail_pos = head_pos - direction_dict[direction]
        
        visited_positions.add(tail_pos)

end_time_1 = timer()

print(len(visited_positions))
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
