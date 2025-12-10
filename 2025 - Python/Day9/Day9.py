from timeit import default_timer as timer
import math as m

def contour_fill(map_edges, contour):
    min_row, max_row, min_col, max_col = map_edges
    new_tiles = set()

    for r in range(min_row, max_row+1):
        inside_flag = -1
        for c in range(min_col-1, max_col+2):
            if (r,c) not in contour and (r,c-1) in contour and ((r-1,c) in new_tiles or (r-1,c) in contour):
                inside_flag *= -1
            
            if inside_flag==1:
                new_tiles.add((r,c))
    
    contour.update(new_tiles)

    return contour

def flood_fill(map_edges, contour):
    min_row, _, min_col, _ = map_edges

    r, c = min_row+10, min_col
    while True:
        if complex(r,c) not in contour and complex(r,c-1) in contour:
            init_tile = complex(r,c)
            break
        else:
            c += 1

    filled_set = {init_tile}
    open_set = {init_tile}
    neighbors = {1,-1,1j,-1j}

    while open_set:
        current_tile = open_set.pop()

        for n in neighbors:
            nb = current_tile + n

            if nb not in contour and nb not in filled_set:
                filled_set.add(nb)
                open_set.add(nb)

    filled_set.update(contour)

    return filled_set





start_time = timer()

DAY_NUMBER = 9
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    red_tiles = [complex(int(l.strip().split(',')[0]), int(l.strip().split(',')[1])) for l in file]

max_area = 0

for i,t in enumerate(red_tiles):
    for t2 in red_tiles[i+1:]:
        area = (abs(t.real-t2.real) + 1) * (abs(t.imag-t2.imag) + 1)
        max_area = area if area>max_area else max_area

green_tiles = set()
min_row, max_row = m.inf, 0
min_col, max_col = m.inf, 0

for i in range(len(red_tiles)):
    c1,r1 = int(red_tiles[i-1].real), int(red_tiles[i-1].imag)
    c2,r2 = int(red_tiles[i].real), int(red_tiles[i].imag)

    row1, col1 = min(r1,r2), min(c1,c2)
    row2, col2 = max(r1,r2), max(c1,c2)

    min_row = row1 if row1<min_row else min_row
    max_row = row1 if row1>max_row else max_row
    min_col = col1 if col1<min_col else min_col
    max_col = col1 if col1>max_col else max_col

    if row1==row2:
        green_tiles.update(set(complex(row1,c) for c in range(col1,col2+1)))
    else:
        green_tiles.update(set(complex(r,col1) for r in range(row1,row2+1)))

green_tiles = flood_fill((min_row,max_row,min_col,max_col), green_tiles)

# test = [['#' if complex(r,c) in green_tiles else '.' for c in range(13)] for r in range(10)]

end_time = timer()

print(int(max_area))
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
