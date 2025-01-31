from timeit import default_timer as timer

# def find_all_paths(pos, drc, goal_loc, map_dict):
#     """
#     Find the lengths of all paths from start to goal recursively
#     """

#     diffs = {1, 1j, -1, -1j}
#     out_dict = {1: 'v', -1: '^', 1j: '>', -1j: '<'}

#     path_length = 1
#     next_path_lengths = []

#     while True:
#         new_drcs = diffs.difference({-drc})
#         neighbors = [(pos + d, d, map_dict[pos + d]) for d in new_drcs if map_dict[pos + d] in {'.', out_dict[d]}]

#         if len(neighbors)==1:
#             pos, drc, _ = neighbors[0]

#             if pos==goal_loc:
#                 return path_length

#             path_length += 1
#         else:
#             for neighbor_pos, neighbor_dir, _ in neighbors:
#                 tmp = find_all_paths(neighbor_pos, neighbor_dir, goal_loc, map_dict)
#                 if isinstance(tmp, int):
#                     next_path_lengths.append(tmp)
#                 else:
#                     next_path_lengths += tmp

#             return [path_length + next_length for next_length in next_path_lengths]

def make_forest_graph(start_loc, start_drc, goal_loc, map_dict, graph_dict):
    """
    Make a graph that shows, for each crossroads, the distance to connected crossroads
    """

    drcs, out_drcs = {1, 1j, -1, -1j}, {1: 'v', -1: '^', 1j: '>', -1j: '<'}
    stack, num_out = {(start_loc, start_drc): None}, {}

    while stack:
        start_pos, start_drc = next(iter(stack))
        del stack[(start_pos, start_drc)]

        path_len, goal_flag = 1, 0

        new_drcs = drcs.difference({-start_drc})
        neighbors = sum(1 for d in new_drcs if map_dict[start_pos+d]!='#')
        out_neighbors = [(start_pos+d, d) for d in new_drcs if map_dict[start_pos+d] in {'.', out_drcs[d]}]

        while neighbors==1:
            pos, drc = out_neighbors[0]

            if pos==goal_loc:
                path_len += 1
                goal_flag = 1
                break

            path_len += 1
            new_drcs = drcs.difference({-drc})
            neighbors = sum(1 for d in new_drcs if map_dict[pos+d]!='#')
            out_neighbors = [(pos+d, d) for d in new_drcs if map_dict[pos+d] in {'.', out_drcs[d]}]

        num_out[pos] = len(out_neighbors)

        graph_dict = add_to_graph_dict(start_pos - start_drc, pos, path_len, graph_dict)

        if goal_flag:
            continue

        for pos, drc in out_neighbors:
            if pos-drc not in graph_dict or len(graph_dict[pos-drc])<num_out[pos-drc]:
                stack[(pos, drc)] = None

    return graph_dict

def add_to_graph_dict(start_pos, curr_pos, path_len, graph_dict):
    """
    Add graph vertex to dict
    """
    if start_pos not in graph_dict:
        graph_dict[start_pos] = [(curr_pos, path_len)]
    else:
        graph_dict[start_pos].append((curr_pos, path_len))

    return graph_dict





start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_23.txt'
INPUT_NAME = 'Inputs/Input_2023_23.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

MAX_MAP_INDEX = len(file_lines) - 1
forest_map = {complex(i_r, i_c): c for i_r, r in enumerate(file_lines) for i_c, c in enumerate(r)}
forest_graph = {}

START = complex(0, 1)
START_DIR = 1
GOAL = complex(MAX_MAP_INDEX, MAX_MAP_INDEX - 1)

# paths = find_all_paths(START, START_DIR, GOAL, forest_map)
forest_graph = make_forest_graph(START, START_DIR, GOAL, forest_map, forest_graph)

# ans1 = max(paths)

end_time_1 = timer()

# print(ans1)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# Part II

start_time_2 = timer()

ans2 = 0

# Change possible 

end_time_2 = timer()

print(ans2)
print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
