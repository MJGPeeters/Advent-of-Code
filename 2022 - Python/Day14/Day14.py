from timeit import default_timer as timer

def falling_sand(tile_map, lowest_stone_height):
    sand_pos_x = 500
    sand_pos_y = 0

    while True:
        if (sand_pos_x, sand_pos_y + 1) not in tile_map:
            sand_pos_y += 1
            if sand_pos_y > lowest_stone_height:
                return 0, tile_map
        elif (sand_pos_x - 1, sand_pos_y + 1) not in tile_map:
            sand_pos_x -= 1
            sand_pos_y += 1
        elif (sand_pos_x + 1, sand_pos_y + 1) not in tile_map:
            sand_pos_x += 1
            sand_pos_y += 1
        else:
            tile_map[(sand_pos_x, sand_pos_y)] = 1
            return 1, tile_map

start_time_1 = timer()

DAY_NUMBER = 14
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    scans = [line.strip() for line in file]

rock_dict = {}
max_y = 0

for scan in scans:
    vertices = scan.split(' -> ')
    vertex_list = []

    for i in range(len(vertices)-1):
        x_1, y_1 = map(int, vertices[i].split(','))
        x_2, y_2 = map(int, vertices[i+1].split(','))
    
        x_s, x_e = min(x_1, x_2), max(x_1, x_2)
        y_s, y_e = min(y_1, y_2), max(y_1, y_2)

        if x_s==x_e:
            for y in range(y_s, y_e+1):
                rock_dict[(x_s,y)] = 1
        else:
            for x in range(x_s, x_e+1):
                rock_dict[(x,y_s)] = 1
        
        if y_e>max_y:
            max_y = y_e

num_units = 0
rest_bool = 1

while rest_bool:
    rest_bool, rock_dict = falling_sand(rock_dict, max_y)
    num_units += rest_bool

end_time_1 = timer()

print(num_units)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
