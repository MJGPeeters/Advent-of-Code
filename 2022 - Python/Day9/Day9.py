from timeit import default_timer as timer
import math as m
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
rope_pos = [0,0,0,0,0,0,0,0,0,0]
visited_positions_short = {0}
visited_positions_long = {0}

for motion in motions:
    direction_str, amount = motion.split()
    direction = direction_dict[direction_str]

    # Part 1
    for i in range(int(amount)):
        head_pos += direction

        if abs(tail_pos.real-head_pos.real)>1 or abs(tail_pos.imag-head_pos.imag)>1:
            tail_pos = head_pos - direction
        
        visited_positions_short.add(tail_pos)

    # Part 2
    for i in range(int(amount)):
        rope_pos[0] += direction

        for knot in range(1,len(rope_pos)):
            prev_knot_pos = rope_pos[knot-1]
            curr_knot_pos = rope_pos[knot]

            diff = prev_knot_pos - curr_knot_pos

            if abs(diff)<2:
                break
            elif abs(diff)==2 or abs(diff)>2.5:
                movement = diff/2
            else:
                movement = m.copysign(1,diff.real) + 1j*m.copysign(1,diff.imag)

            new_pos = curr_knot_pos + movement
            rope_pos[knot] = int(new_pos.real) + 1j*int(new_pos.imag)
        
        visited_positions_long.add(rope_pos[-1])

end_time_1 = timer()

print(len(visited_positions_short))
print(len(visited_positions_long))
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
