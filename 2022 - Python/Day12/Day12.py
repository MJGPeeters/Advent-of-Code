from timeit import default_timer as timer
import math as m
import cmath as cm

# For Part 2 it is easiest to reverse the problem, so to start the search at 'E' and then 
# find the shortest route to an 'a'. Therefore, this method is used for both Part 1 & 2. 

def dijkstra_height(input_map, goal='S'):
    height_map = []
    dist_map = [[m.inf for _ in line] for line in input_map]
    
    for row_idx, row in enumerate(input_map):
        if 'S' in row and 'E' in row:
            col_idx_s = row.find('S')
            S_pos = (row_idx, col_idx_s)
            col_idx_e = row.find('E')
            dist_map[row_idx][col_idx_e] = 0
            init_pos = (row_idx, col_idx_e)
            height_map.append('a' + input_map[row_idx][1:col_idx_e] + 'z' + input_map[row_idx][col_idx_e+1:])

        elif 'S' in row:
            col_idx_s = row.find('S')
            S_pos = (row_idx, col_idx_s)
            height_map.append(input_map[row_idx][0:col_idx_s] + 'a' + input_map[row_idx][col_idx_s+1:])

        elif 'E' in row:
            col_idx_e = row.find('E')
            dist_map[row_idx][col_idx_e] = 0
            init_pos = (row_idx, col_idx_e)
            height_map.append(input_map[row_idx][0:col_idx_e] + 'z' + input_map[row_idx][col_idx_e+1:])
        
        else:
            height_map.append(input_map[row_idx])

    min_row, max_row = 0, len(height_map)-1
    min_col, max_col = 0, len(height_map[0])-1

    open_set = [init_pos]

    while open_set:
        cur_sqr = open_set.pop(0)
        cur_dst = dist_map[cur_sqr[0]][cur_sqr[1]]

        if goal=='S':
            if cur_sqr==S_pos:
                return dist_map[cur_sqr[0]][cur_sqr[1]]
        else:
            if height_map[cur_sqr[0]][cur_sqr[1]]==goal:
                return dist_map[cur_sqr[0]][cur_sqr[1]]
                
        ngbs = [(cur_sqr[0] + 0, cur_sqr[1] + 1),
                     (cur_sqr[0] + 0, cur_sqr[1] - 1),
                     (cur_sqr[0] + 1, cur_sqr[1] + 0),
                     (cur_sqr[0] - 1, cur_sqr[1] + 0)]

        for ngb in ngbs:
            # Check if neighbor is not out of bounds
            if (ngb[0] < min_row or ngb[0] > max_row) or (ngb[1] < min_col or ngb[1] > max_col):
                continue
            
            # Check if elevation difference to neighbor is not too big
            if ord(height_map[ngb[0]][ngb[1]]) - ord(height_map[cur_sqr[0]][cur_sqr[1]]) < -1:
                continue

            if cur_dst + 1 < dist_map[ngb[0]][ngb[1]]:
                dist_map[ngb[0]][ngb[1]] = cur_dst + 1
                open_set.append(ngb)

start_time_1 = timer()

DAY_NUMBER = 12
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    heightmap = [line.strip() for line in file]

num_steps_S = dijkstra_height(heightmap)
num_steps_a = dijkstra_height(heightmap, 'a')

end_time_1 = timer()

print(num_steps_S)
print(num_steps_a)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
