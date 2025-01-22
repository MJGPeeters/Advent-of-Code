from timeit import default_timer as timer
from collections import deque
import itertools
import heapq as hp

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_17.txt'
INPUT_NAME = 'Inputs/Input_2023_17.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

def pathfinding_crucible(map_array, start, goal, min_steps, max_steps):
    """
    Find the heat loss for a crucible with given minimum and maximum succesive steps in a direction
    """

    MAP_LIMIT = len(map_array) - 1
    MIN_RANGE, MAX_RANGE = min_steps, max_steps + 1

    g_score, origin_dict, open_set = {}, {}, []

    for direction, num_steps in itertools.product(((1, 0), (0, 1)), range(MIN_RANGE, MAX_RANGE)):
        next_node = tuple(n + d*num_steps for n, d in zip(start, direction))
        i_steps = tuple((start[0] + direction[0]*s, start[1] + direction[1]*s) for s in range(1, num_steps+1))
        tmp_g_score = sum((map_array[i_row][i_col] for i_row, i_col in i_steps))
        g_score[(next_node, direction)] = tmp_g_score
        hp.heappush(open_set, (tmp_g_score, (next_node, direction)))

    while open_set:
        node, prev_direction = hp.heappop(open_set)[1]

        if node==goal:
            return g_score[(node, prev_direction)]

        directions = ((prev_direction[1], prev_direction[0]), (-prev_direction[1], -prev_direction[0]))

        for direction, num_steps in itertools.product(directions, range(MIN_RANGE, MAX_RANGE)):
            new_node = tuple(n + d*num_steps for n, d in zip(node, direction))

            if not (0<=new_node[0]<=MAP_LIMIT and 0<=new_node[1]<=MAP_LIMIT):
                continue

            i_steps = tuple((node[0] + direction[0]*s, node[1] + direction[1]*s) for s in range(1, num_steps + 1))
            tmp_g_score = g_score[(node, prev_direction)] + sum(
                                                    (map_array[i_row][i_col] for i_row, i_col in i_steps))

            if (new_node, direction) not in g_score:
                origin_dict[(new_node, direction)] = (node, prev_direction)
                g_score[(new_node, direction)] = tmp_g_score
                hp.heappush(open_set, (g_score[(new_node, direction)], (new_node, direction)))
            elif  tmp_g_score<g_score[(new_node, direction)]:
                origin_dict[(new_node, direction)] = (node, prev_direction)
                g_score[(new_node, direction)] = tmp_g_score
                hp.heappush(open_set, (g_score[(new_node, direction)], (new_node, direction)))

heat_loss_map, path_map = [], []
map_size = len(file_lines) - 1

for line in file_lines:
    heat_loss_map.append([int(v) for v in line])
    path_map.append(['.' for v in line])

heat_loss_1 = pathfinding_crucible(heat_loss_map, (0,0), (map_size, map_size), 1, 3)

endTime1 = timer()

print(heat_loss_1)
print(f'Time elapsed: {endTime1 - start_time_1:.6f} s')

# Part II

start_time_2 = timer()

heat_loss_2 = pathfinding_crucible(heat_loss_map, (0,0), (map_size, map_size), 4, 10)

end_time_2 = timer()

print(heat_loss_2)
print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
