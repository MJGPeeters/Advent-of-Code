from timeit import default_timer as timer
from collections import deque
import itertools
import heapq as hp
import math as m

startTime1 = timer()

TEST_NAME = 'Tests/Test_2023_17.txt'
INPUT_NAME = 'Inputs/Input_2023_17.txt'

with open(TEST_NAME, "r") as file:
    file_lines = file.read().splitlines()

def pathfinding_crucible(map_array, start, initial_direction, goal):
    """
    Find the shortest path from start to goal for a given mapArray
    """

    map_limit = len(map_array) - 1

    g_score = [[m.inf for element in row] for row in map_array]
    g_score[start[0]][start[1]] = 0

    open_set = []
    hp.heappush(open_set, (g_score[start[0]][start[1]], (start, initial_direction)))

    origin_dict = {}

    while open_set:
        node, previous_direction = hp.heappop(open_set)[1]

        if node==goal:
            return reconstruct_path_crucible(origin_dict, (node, previous_direction)), g_score[node[0]][node[1]]

        directions = ((previous_direction[1], previous_direction[0]), 
                      (-previous_direction[1], -previous_direction[0]))

        for direction, num_steps in itertools.product(directions, range(1,4)):
            tst_node = tuple(n + d*num_steps for n, d in zip(node, direction))

            if not (0<=tst_node[0]<=map_limit and 0<=tst_node[1]<=map_limit):
                continue

            i_steps = tuple((node[0] + direction[0]*s, node[1] + direction[1]*s) for s in range(1, num_steps + 1))
            tmp_g_score = g_score[node[0]][node[1]] + sum((map_array[i_row][i_col] for i_row, i_col in i_steps))

            if tmp_g_score<g_score[tst_node[0]][tst_node[1]]:
                origin_dict[(tst_node, direction)] = (node, previous_direction)
                g_score[tst_node[0]][tst_node[1]] = tmp_g_score

                # if tst_node not in open_set:
                hp.heappush(open_set, (g_score[tst_node[0]][tst_node[1]], (tst_node, direction)))

    return None

def reconstruct_path_crucible(dictionary, node):
    """
    Return the reconstructed path from your pathfinding algorithm
    """

    reconstructed_path = deque()
    reconstructed_path.appendleft(node[0])

    while node in dictionary:
        node = dictionary[node]
        reconstructed_path.appendleft(node[0])

    return reconstructed_path

heat_loss_map, path_map = [], []
map_size = len(file_lines) - 1

for line in file_lines:
    heat_loss_map.append([int(v) for v in line])
    path_map.append(['.' for v in line])

path, heat_loss = pathfinding_crucible(heat_loss_map, (0,0), (-1, 0), (map_size, map_size))

for r, c in path:
    path_map[r][c] = 'X'

# Option 1: Take into account previous steps in pathfinding algorithm (a given node is not just
#           determined by its coordinates, but also by the previous three directions). This way,
#           there can be multiple ways to arrive at a certain coordinate. If the test_node would
#           result in four directions that are the same, the node is not admissable.

# Option 2: For every node, you can only rotate left or right from your current direction, not go
#           straight. Check one, two or three steps in that direction. For this the current
#           direction needs to be saved as well.

# Try option 2 first, seems the easiest to implement and maybe also faster.

endTime1 = timer()

print(heat_loss)
print(f'Time elapsed: {endTime1 - startTime1:.6f} s')

# # Part II

# startTime2 = timer()

# ans2 = 0



# endTime2 = timer()

# print(ans2)
# print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
