from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 8
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

def is_tree_visible(tree_map,row,col):
    map_size = len(tree_map)
    visible_from_left, visible_from_right = 1, 1
    visible_from_top, visible_from_bottom = 1, 1
    tree_size = tree_map[row][col]

    # Check if visible from left
    for i in range(col):
        tmp = tree_map[row][i]
        if tree_size<=tree_map[row][i]:
            visible_from_left = 0
            break
    if visible_from_left:
        return 1

    # Check if visible from right
    for i in range(map_size-1,col,-1):
        if tree_size<=tree_map[row][i]:
            visible_from_right = 0
            break
    if visible_from_right:
        return 1

    # Check if visible from top
    for i in range(row):
        if tree_size<=tree_map[i][col]:
            visible_from_top = 0
            break
    if visible_from_top:
        return 1

    # Check if visible from bottom
    for i in range(map_size-1,row,-1):
        if tree_size<=tree_map[i][col]:
            visible_from_bottom = 0
            break
    if visible_from_bottom:
        return 1
    
    return 0

def find_scenic_score(tree_map,row,col):
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
    
    return visible_trees_left*visible_trees_right*visible_trees_top*visible_trees_bottom

with open(FILE_NAME, 'r') as file:
    tree_map = [line.strip() for line in file]

map_size = len(tree_map)
visible_trees = 4*(map_size-1)
max_scenic_score = 0

for i in range(1,map_size-1):
    for j in range(1,map_size-1):
        visible_trees += is_tree_visible(tree_map,i,j)

for i in range(1,map_size-1):
    for j in range(1,map_size-1):
        scenic_score = find_scenic_score(tree_map,i,j)
        if scenic_score>max_scenic_score:
            max_scenic_score = scenic_score

end_time_1 = timer()

print(visible_trees)
print(max_scenic_score)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
