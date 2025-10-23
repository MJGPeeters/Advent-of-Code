from timeit import default_timer as timer
import copy

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
        graph_dict[start_pos] = {(curr_pos, path_len)}
    else:
        graph_dict[start_pos].add((curr_pos, path_len))

    return graph_dict

def longest_path_I(start_loc, goal_loc, graph_dict):
    """
    Find longest path from start to goal in graph
    """

    u_paths = {(0, start_loc)}
    f_paths = set()

    while u_paths:
        tmp_len, tmp_loc = u_paths.pop()
        next = graph_dict[tmp_loc]

        for next_p, l in next:
            f_paths.add(tmp_len + l-1) if next_p==goal_loc else u_paths.add((tmp_len + l, next_p))

    return max(f_paths)

def expand_graph(graph_dict):
    """
    Expand graph from directed to undirected
    """

    expanded_graph = copy.copy(graph_dict)

    for prev_pos, vals in graph_dict.items():
        for next_pos, length in vals:
            expanded_graph = add_to_graph_dict(next_pos, prev_pos, length, expanded_graph)

    return expanded_graph

def longest_path_II(start_loc, goal_loc, graph_dict):
    """
    Find longest path from start to goal in graph
    """

    u_paths = [(0, start_loc, set())]
    f_paths = set()

    while u_paths:
        tmp_len, tmp_loc, prev_locs = u_paths.pop()
        next = graph_dict[tmp_loc]

        for next_p, l in next:
            if next_p==goal_loc:
                f_paths.add(tmp_len + l-1)
            elif next_p not in prev_locs:
                prev_locs.add(tmp_loc)
                u_paths.append((tmp_len + l, next_p, prev_locs))

    return max(f_paths)

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_23.txt'
INPUT_NAME = 'Inputs/Input_2023_23.txt'

with open(TEST_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

MAX_MAP_INDEX = len(file_lines) - 1
forest_map = {complex(i_r, i_c): c for i_r, r in enumerate(file_lines) for i_c, c in enumerate(r)}
forest_graph = {}

START = complex(0, 1)
START_DIR = 1
GOAL = complex(MAX_MAP_INDEX, MAX_MAP_INDEX - 1)

forest_graph = make_forest_graph(START, START_DIR, GOAL, forest_map, forest_graph)
ans1 = longest_path_I(START - START_DIR, GOAL, forest_graph)

end_time_1 = timer()

print(ans1)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# Part II

start_time_2 = timer()

# Very similar algorithm as part I

# Make a different graph_dict, now with every neighbor for a crossroads
dry_forest_graph = expand_graph(forest_graph)

# When arriving at a crossroads, try every neighbor
# Check if neighbor is already in path, if so abort that path
# If not, increase path length, add current position to history, add neighbor as current furthest point
# Find longest path in the end
ans2 = longest_path_II(START - START_DIR, GOAL, dry_forest_graph)

end_time_2 = timer()

print(ans2)
print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
