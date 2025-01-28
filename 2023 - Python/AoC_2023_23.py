from timeit import default_timer as timer
import copy

def find_all_paths(start_loc, goal_loc, map_dict):
    """
    Find the lengths of all paths from start to goal recursively
    """

    diffs = (1, complex(0,1), -1, complex(0,-1))
    out_dict = {1: 'v', -1: '^', 1j: '>', -1j: '<'}

    pos = start_loc
    map_dict[pos] = '#'

    path_length = 1
    next_path_lengths = []

    while True:
        neighbors = [(pos + d, d, map_dict[pos + d]) for d in diffs if map_dict[pos + d] in {'.', out_dict[d]}]

        if len(neighbors)==1:
            pos, _, _ = neighbors[0]

            if pos==goal_loc:
                return path_length

            map_dict[pos] = '#'
            path_length += 1
        else:
            for pos, _, _ in neighbors:
                new_map_dict = copy.copy(map_dict)
                tmp = find_all_paths(pos, goal_loc, new_map_dict)
                if isinstance(tmp, int):
                    next_path_lengths.append(tmp)
                else:
                    next_path_lengths += tmp

            out = [path_length + next_length for next_length in next_path_lengths]
            return out

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_23.txt'
INPUT_NAME = 'Inputs/Input_2023_23.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

FOREST_SIZE = len(file_lines)
forest_map = {complex(i_r, i_c): c for i_r, r in enumerate(file_lines) for i_c, c in enumerate(r)}
forest_map[1j] = '#'

START = complex(1, 1)
GOAL = complex(FOREST_SIZE - 1, FOREST_SIZE - 2)

paths = find_all_paths(START, GOAL, forest_map)

ans1 = max(paths) + 1
# First go through the map and find all the crossroads. For every crossroads, check how many
# roads go into and out of the crossroads. Only consider the crossroads with multiple roads
# going out.


# for i_row, row in enumerate(FOREST_MAP):
#     for i_col, col in enumerate(row):
#         if col=='.' and FOREST_MAP[i_row][i_col]!='.'

# crossroads = [(r,c) for r in FOREST_MAP for c in r if c=='.' and ]

# For all those crossroads, find to what other crossroads they connect, and what the distance
# between them is.

# Make a graph of this, stored in a dictionary:
#       {crossroads coordinates: (distance, (next crossroads coordinates))}
#       {(2, 3): (10, (5, 8)), (15, (8, 12))}

# Then start at the initial position, find the first crossroads (and distance to it). From there,
# every time you encounter a crossroads, check both paths by looking up in the dictionary where
# they lead. Do this recursively, until all paths end at the goal coordinates (or reach a dead end).


# Check which path has the longest length.

end_time_1 = timer()

print(ans1)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# # Part II

# start_time_2 = timer()

# ans2 = 0



# end_time_2 = timer()

# print(ans2)
# print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
