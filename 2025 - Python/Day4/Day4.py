from timeit import default_timer as timer
import cmath

start_time = timer()

DAY_NUMBER = 4
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    paper_map = {complex(row,col) for row, line in enumerate(file) for col, element in enumerate(line) if element=='@'}

neighbors = {1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j}
num_rolls = 0

for roll in paper_map:
    if sum(neighbor+roll in paper_map for neighbor in neighbors)<4:
        num_rolls += 1

end_time = timer()

print(num_rolls)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
