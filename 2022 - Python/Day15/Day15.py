from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 15
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
    BEACON_ROW_TEST = 10
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"
    BEACON_ROW_TEST = 2000000

with open(FILE_NAME, 'r') as file:
    sensor_beacon_locations = [line.strip() for line in file]

x_ranges = []
test_row_beacons = set()

for loc in sensor_beacon_locations:
    loc_split = loc.split()
    sensor_x = int(loc_split[2][2:-1])
    sensor_y = int(loc_split[3][2:-1])
    beacon_x = int(loc_split[8][2:-1])
    beacon_y = int(loc_split[9][2:])

    if beacon_y==BEACON_ROW_TEST:
        test_row_beacons.add((beacon_x, beacon_y))

    sensor_beacon_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    sensor_row_dist = abs(sensor_y - BEACON_ROW_TEST)
    row_beacon_dist = sensor_beacon_dist - sensor_row_dist

    if row_beacon_dist<=0:
        continue

    new_range = (sensor_x - row_beacon_dist, sensor_x + row_beacon_dist)

    if not x_ranges:
        x_ranges = [new_range]
        continue

    new_x_ranges = []

    for idx, x_range in enumerate(x_ranges):
        if new_range[0]<x_range[0]:
            if new_range[1]<x_range[0]-1:
                new_x_ranges.append(x_range)
            else:
                new_range = (new_range[0], max(new_range[1], x_range[1]))
        elif new_range[0]<=x_range[1]+1:
            new_range = (x_range[0], max(new_range[1], x_range[1]))
        else:
            new_x_ranges.append(x_range)
    
    new_x_ranges.append(new_range)
    x_ranges = new_x_ranges

forbidden_positions = -len(test_row_beacons)

for x_range in x_ranges:
    forbidden_positions += abs(x_range[0] - x_range[1]) + 1

end_time_1 = timer()

print(forbidden_positions)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
