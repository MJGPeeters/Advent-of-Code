"""
Pathfinding algorithms

a_star: Implementation of A* algorithm
reconstruct_path: Reconstruct path found by pathfinding algorithm
manhattan_distance: Calculate Manhattan distance
"""

from collections import deque
import heapq as hp
import math as m

def manhattan_distance(start, goal):
    """
    Calculate Manhattan distance between start and goal, assuming two dimensions
    """
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def reconstruct_path(dictionary, node):
    """
    Return the reconstructed path from your pathfinding algorithm
    """

    reconstructed_path = deque()
    reconstructed_path.appendleft(node)

    while node in dictionary:
        node = dictionary[node]
        reconstructed_path.appendleft(node)

    return reconstructed_path

def a_star(map_array, start, goal, h):
    """
    Find the shortest path from start to goal for a given mapArray
    """

    map_limit = len(map_array) - 1

    g_score = [[m.inf for element in row] for row in map_array]
    g_score[start[0]][start[1]] = 0

    f_score = [[m.inf for element in row] for row in map_array]
    f_score[start[0]][start[1]] = h(start, goal)

    open_set = []
    hp.heappush(open_set, (f_score[start[0]][start[1]], start))

    origin_dict = dict()

    while open_set:
        node = hp.heappop(open_set)[1]

        if node==goal:
            return reconstruct_path(origin_dict, node)

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for direction in directions:
            test_node = tuple(n + d for n, d in zip(node, direction))

            if not (0<=test_node[0]<=map_limit and 0<=test_node[1]<=map_limit):
                continue

            tmp_g_score = g_score[node[0]][node[1]] + 1

            if tmp_g_score<g_score[test_node[0]][test_node[1]]:
                origin_dict[test_node] = node
                g_score[test_node[0]][test_node[1]] = tmp_g_score
                f_score[test_node[0]][test_node[1]] = tmp_g_score + h(test_node, goal)

                if test_node not in open_set:
                    hp.heappush(open_set, (f_score[test_node[0]][test_node[1]], test_node))

    return None
