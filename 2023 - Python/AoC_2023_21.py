from timeit import default_timer as timer
import heapq as hp

def garden_steps(starting_point, map_array, max_steps):
    """
    Find the shortest number of steps to reach each tile in map
    """

    MAP_SIZE = len(map_array) - 1

    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # point_heap ncludes all points in the area, for which neighbors are not yet checked
    point_heap = []
    hp.heappush(point_heap, (0, starting_point))

    # Least steps is a dict that keeps track of the least amount of steps to reach a point
    least_steps = {starting_point: 0}

    # Continue with loop until point_heap is empty (all neighbors are checked)
    while len(point_heap):
        curr_point = hp.heappop(point_heap)[1]

        steps = least_steps[curr_point]

        # Check all four neighbors
        for diff in neighbors:
            next_point = curr_point[0] + diff[0], curr_point[1] + diff[1]
            next_steps = steps + 1

            if not (0<=next_point[0]<=MAP_SIZE and 0<=next_point[1]<=MAP_SIZE):
                continue

            if next_point in least_steps or map_array[next_point[0]][next_point[1]]=='#':
                continue

            least_steps[next_point] = next_steps

            if next_steps!=max_steps:
                hp.heappush(point_heap, (next_steps, next_point))

    return least_steps

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_21.txt'
INPUT_NAME = 'Inputs/Input_2023_21.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

GARDEN_MAP_SIZE = len(file_lines) - 1
MAX_STEPS = 26501365

garden_map = [list(line) for line in file_lines]

starting_point = [(i_r, i_c) for i_r, r in enumerate(garden_map) for i_c, c in enumerate(r) if c=='S']

steps_dict = garden_steps(starting_point[0], garden_map, GARDEN_MAP_SIZE/2)

num_plots_1 = sum(1 for val in steps_dict.values() if (val % 2)==0)

end_time_1 = timer()

print(num_plots_1)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# Part II

start_time_2 = timer()

L = int((MAX_STEPS - GARDEN_MAP_SIZE/2) // (GARDEN_MAP_SIZE+1))

A_ALL = garden_steps(starting_point[0], garden_map, GARDEN_MAP_SIZE)
A = sum(1 for val in A_ALL.values() if (val % 2)==1)
C = sum(1 for val in steps_dict.values() if (val % 2)==1)

# Center wedges
DOWN_WEDGE_ALL = garden_steps((0, int(GARDEN_MAP_SIZE/2)), garden_map, GARDEN_MAP_SIZE)
UP_WEDGE_ALL = garden_steps((GARDEN_MAP_SIZE, int(GARDEN_MAP_SIZE/2)), garden_map, GARDEN_MAP_SIZE)
RIGHT_WEDGE_ALL = garden_steps((int(GARDEN_MAP_SIZE/2), 0), garden_map, GARDEN_MAP_SIZE)
LEFT_WEDGE_ALL = garden_steps((int(GARDEN_MAP_SIZE/2), GARDEN_MAP_SIZE), garden_map, GARDEN_MAP_SIZE)

DOWN_WEDGE = sum(1 for val in DOWN_WEDGE_ALL.values() if (val % 2)==1)
UP_WEDGE = sum(1 for val in UP_WEDGE_ALL.values() if (val % 2)==1)
RIGHT_WEDGE = sum(1 for val in RIGHT_WEDGE_ALL.values() if (val % 2)==1)
LEFT_WEDGE = sum(1 for val in LEFT_WEDGE_ALL.values() if (val % 2)==1)
WEDGES = DOWN_WEDGE + UP_WEDGE + RIGHT_WEDGE + LEFT_WEDGE

# Small corners
UL_CORNER_S_ALL = garden_steps((0, 0), garden_map, int(GARDEN_MAP_SIZE/2))
DL_CORNER_S_ALL = garden_steps((GARDEN_MAP_SIZE, 0), garden_map, int(GARDEN_MAP_SIZE/2))
UR_CORNER_S_ALL = garden_steps((0, GARDEN_MAP_SIZE), garden_map, int(GARDEN_MAP_SIZE/2))
DR_CORNER_S_ALL = garden_steps((GARDEN_MAP_SIZE, GARDEN_MAP_SIZE), garden_map, int(GARDEN_MAP_SIZE/2))

UL_CORNER_S = sum(1 for val in UL_CORNER_S_ALL.values() if (val % 2)==0)
DL_CORNER_S = sum(1 for val in DL_CORNER_S_ALL.values() if (val % 2)==0)
UR_CORNER_S = sum(1 for val in UR_CORNER_S_ALL.values() if (val % 2)==0)
DR_CORNER_S = sum(1 for val in DR_CORNER_S_ALL.values() if (val % 2)==0)
CORNERS_S = UL_CORNER_S + DL_CORNER_S + UR_CORNER_S + DR_CORNER_S

# Big corners
UL_CORNER_B_ALL = garden_steps((0, 0), garden_map, int(3*GARDEN_MAP_SIZE/2))
DL_CORNER_B_ALL = garden_steps((GARDEN_MAP_SIZE, 0), garden_map, int(3*GARDEN_MAP_SIZE/2))
UR_CORNER_B_ALL = garden_steps((0, GARDEN_MAP_SIZE), garden_map, int(3*GARDEN_MAP_SIZE/2))
DR_CORNER_B_ALL = garden_steps((GARDEN_MAP_SIZE, GARDEN_MAP_SIZE), garden_map, int(3*GARDEN_MAP_SIZE/2))

UL_CORNER_B = sum(1 for val in UL_CORNER_B_ALL.values() if (val % 2)==0)
DL_CORNER_B = sum(1 for val in DL_CORNER_B_ALL.values() if (val % 2)==0)
UR_CORNER_B = sum(1 for val in UR_CORNER_B_ALL.values() if (val % 2)==0)
DR_CORNER_B = sum(1 for val in DR_CORNER_B_ALL.values() if (val % 2)==0)
CORNERS_B = UL_CORNER_B + DL_CORNER_B + UR_CORNER_B + DR_CORNER_B

num_plots_2 = (2*L**2 - 2*L + 1)*A + WEDGES + L*CORNERS_S + (L - 1)*CORNERS_B

end_time_2 = timer()

print(num_plots_2)
print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
