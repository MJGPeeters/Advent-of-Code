from timeit import default_timer as timer
import math as m
import cmath as cm

def dijkstra_height(height_map, start, end):

    dist_map = [[m.inf for _ in line] for line in height_map]
    dist_map[start[0]][start[1]] = 0

    min_row, max_row = 0, len(height_map)-1
    min_col, max_col = 0, len(height_map[0])-1

    open_set = [start]

    while open_set:
        current_square = open_set.pop(0)
        current_dist = dist_map[current_square[0]][current_square[1]]

        if current_square==end:
            return dist_map[current_square[0]][current_square[1]]

        neighbors = [(current_square[0] + 0, current_square[1] + 1),
                     (current_square[0] + 0, current_square[1] - 1),
                     (current_square[0] + 1, current_square[1] + 0),
                     (current_square[0] - 1, current_square[1] + 0)]

        for neighbor in neighbors:
            # Check if neighbor is not out of bounds
            if (neighbor[0] < min_row or neighbor[0] > max_row) or (neighbor[1] < min_col or neighbor[1] > max_col):
                continue
            
            # Check if elevation difference to neighbor is not too big
            if ord(height_map[neighbor[0]][neighbor[1]]) - ord(height_map[current_square[0]][current_square[1]]) > 1:
                continue

            if current_dist + 1 < dist_map[neighbor[0]][neighbor[1]]:
                dist_map[neighbor[0]][neighbor[1]] = current_dist + 1
                open_set.append(neighbor)


start_time_1 = timer()

DAY_NUMBER = 12
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    heightmap = [line.strip() for line in file]

for row_idx, row in enumerate(heightmap):
    if 'S' in row:
        col_idx = row.find('S')
        start_pos = (row_idx, col_idx)
        heightmap[row_idx] = heightmap[row_idx][0:col_idx] + 'a' + heightmap[row_idx][col_idx+1:]
    if 'E' in row:
        col_idx = row.find('E')
        end_pos = (row_idx, col_idx)
        heightmap[row_idx] = heightmap[row_idx][0:col_idx] + 'z' + heightmap[row_idx][col_idx+1:]

num_steps = dijkstra_height(heightmap, start_pos, end_pos)

end_time_1 = timer()

print(num_steps)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
