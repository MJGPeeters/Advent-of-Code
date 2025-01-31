from timeit import default_timer as timer
import heapq as hp

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_22.txt'
INPUT_NAME = 'Inputs/Input_2023_22.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

brick_heap = []
ans1 = 0

# Read in data, give each brick a name/number (?) and store them in a min_heap, with minimum z-value
# as sorting value. Store as (min_z_value, ((x,y,z)_start, direction, length))
for line in file_lines:
    first, last = line.split('~')

    start_pos = [int(x) for x in first.split(',')]
    end_pos = [int(x) for x in last.split(',')]

    try:
        direction = [int(i) for i, (s, e) in enumerate(zip(start_pos, end_pos)) if s!=e]
        direction = direction[0]
    except IndexError:
        direction = 2

    length = end_pos[direction] - start_pos[direction]

    hp.heappush(brick_heap, (min(start_pos[2], end_pos[2]), start_pos, direction, length))

# Then, go through min_heap, starting with the smallest z-value
# Keep track of the maximum height for each (x,y) position in a height_map (list of lists)
# Place each brick at the lowest possible place, for all (x,y) values check the height_map and place 
# it at the maximum
# 
# Update height_map
# Update dict storing how many bricks (say 2, namely 13 and 16) support the recently placed brick (say 21)
# Update dict storing which bricks are supported by a given brick (dict[13] += 21, dict[16] += 21)

height_map = {}
for r in range(10):
    for c in range(10):
        height_map[(r,c)] = (0, None)

num_bricks = len(brick_heap)
brick_supports = {brick: [] for brick in range(num_bricks)}
brick_supported_by = {}

for brick_label in range(num_bricks):
    z_min, (xs, ys, zs), direction, length = hp.heappop(brick_heap)
    bricks_supported_by = set()

    # Stacked in the z-direction
    if direction==2:
        max_height, prev_brick_label = height_map[(xs,ys)]

        height_map[(xs,ys)] = (max_height + length+1, brick_label)

        brick_supported_by[brick_label] = 1

        try:
            brick_supports[prev_brick_label].append(brick_label)
        except KeyError:
            pass

    elif direction==1:
        heights = [height_map[(xs, y)][0] for y in range(ys, ys + length + 1)]
        max_height = max(heights)

        for i, height in enumerate(heights):
            _, prev_brick_label = height_map[(xs,ys+i)]

            height_map[(xs, ys+i)] = (max_height + 1, brick_label)

            if height<max_height:
                continue

            bricks_supported_by.add(prev_brick_label)

            if prev_brick_label is not None:
                brick_supports[prev_brick_label].append(brick_label)
    else:
        heights = [height_map[(x, ys)][0] for x in range(xs, xs + length + 1)]
        max_height = max(heights)

        for i, height in enumerate(heights):
            _, prev_brick_label = height_map[(xs+i,ys)]
            height_map[(xs+i, ys)] = (max_height + 1, brick_label)

            if height<max_height:
                continue

            bricks_supported_by.add(prev_brick_label)

            if prev_brick_label is not None:
                brick_supports[prev_brick_label].append(brick_label)

    if direction!=2:
        brick_supported_by[brick_label] = len(bricks_supported_by)

bricks_to_fall = {i: [] for i in range(num_bricks)}

# Go through all bricks. For a given brick, check dictionary which bricks it supports. If these
# are only supported by the current brick, it cannot be disintegrated. Otherwise it can.
for brick in range(num_bricks):
    supported_bricks = brick_supports[brick]

    candidate = 1

    for supported_brick in supported_bricks:
        if brick_supported_by[supported_brick]==1:
            bricks_to_fall[brick].append(supported_brick)
            candidate = 0

    if candidate:
        ans1 += 1

end_time_1 = timer()

print(ans1)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# Part II
start_time_2 = timer()

ans2 = 0

def total_falling_bricks(brick):
    """
    Determine total number of bricks that fall due to brick disintegrating
    """

    num_falling_bricks = 1

    for supported_brick in bricks_to_fall[brick]:
        num_falling_bricks += total_falling_bricks(supported_brick)

    return num_falling_bricks

for brick in range(num_bricks):
    ans2 += total_falling_bricks(brick)

end_time_2 = timer()

print(ans2)
print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
