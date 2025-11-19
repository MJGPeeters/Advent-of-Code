from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 8
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

def check_tree_view(tree_map,row,col):
    map_size = len(tree_map)

    distance_left = col
    distance_right = map_size-col-1
    distance_top = row
    distance_bottom = map_size-row-1

    visible_trees_left, visible_trees_right = 0, 0
    visible_trees_top, visible_trees_bottom = 0, 0

    tree_size = tree_map[row][col]

    # Check to the left
    for i in range(col-1,-1,-1):
        visible_trees_left += 1
        if tree_map[row][i]>=tree_size:
            break

    # Check to the right
    for i in range(col+1,map_size):
        visible_trees_right += 1
        if tree_map[row][i]>=tree_size:
            break

    # Check to the top
    for i in range(row-1,-1,-1):
        visible_trees_top += 1
        if tree_map[i][col]>=tree_size:
            break

    # Check to the bottom
    for i in range(row+1,map_size):
        visible_trees_bottom += 1
        if tree_map[i][col]>=tree_size:
            break

    if (visible_trees_left==distance_left       and tree_map[row][0]<tree_size) or \
       (visible_trees_right==distance_right     and tree_map[row][map_size-1]<tree_size) or \
       (visible_trees_top==distance_top         and tree_map[0][col]<tree_size) or \
       (visible_trees_bottom==distance_bottom   and tree_map[map_size-1][col]<tree_size):
        visible_bool = 1
    else:
        visible_bool = 0

    scenic_score = visible_trees_left*visible_trees_right*visible_trees_top*visible_trees_bottom

    return visible_bool, scenic_score

with open(FILE_NAME, 'r') as file:
    tree_map = [line.strip() for line in file]

map_size = len(tree_map)
visible_trees = 4*(map_size-1)
max_scenic_score = 0

for i in range(1,map_size-1):
    for j in range(1,map_size-1):
        visible_bool, scenic_score = check_tree_view(tree_map,i,j)
        visible_trees += visible_bool
        if scenic_score>max_scenic_score:
            max_scenic_score = scenic_score

end_time_1 = timer()

print(visible_trees)
print(max_scenic_score)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
