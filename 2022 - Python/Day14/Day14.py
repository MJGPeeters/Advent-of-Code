from timeit import default_timer as timer



start_time_1 = timer()

DAY_NUMBER = 14
TEST = True

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    scans = [line.strip() for line in file]

rock_dict = {}

for scan in scans:
    vertices = scan.split(' -> ')
    vertex_list = []

    for i in range(len(vertices)-1):
        x_1, y_1 = map(int, vertices[i].split(','))
        x_2, y_2 = map(int, vertices[i+1].split(','))
    
        x_s, x_e = min(x_1, x_2), max(x_1, x_2)
        y_s, x_e = min(y_1, y_2), max(y_1, y_2)

        if x_s==x_e:
            x = x_s
            for y in range(y_s, y_e+1):
                rock_dict[(x,y)] = 1
        else:
            y = y_s
            for x in range(x_s, x_e+1):
                rock_dict[(x,y)] = 1

        

num_units = 0

end_time_1 = timer()

print(num_units)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
