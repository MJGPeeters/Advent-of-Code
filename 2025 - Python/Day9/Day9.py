from timeit import default_timer as timer

start_time = timer()

DAY_NUMBER = 9
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    red_tiles = [tuple(int(pos) for pos in line.strip().split(',')) for line in file]

max_area = 0

for idx, (row, col) in enumerate(red_tiles):
    for row2, col2 in red_tiles[idx+1:]:
        area = (abs(row2-row) + 1) * (abs(col2-col) + 1)
        max_area = area if area>max_area else max_area

end_time = timer()

print(max_area)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
