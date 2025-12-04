from timeit import default_timer as timer

start_time = timer()

DAY_NUMBER = 4
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    paper_map = {complex(row,col):1 for row, line in enumerate(file) for col, element in enumerate(line) if element=='@'}

neighbors = {1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j}
num_rolls_p1, num_rolls_p2 = 0, 0

for roll in paper_map:
    if sum(neighbor+roll in paper_map for neighbor in neighbors)<4:
        num_rolls_p1 += 1

while True:
    removable_rolls = set()

    for roll in paper_map:
        if sum(neighbor+roll in paper_map for neighbor in neighbors)<4:
            removable_rolls.add(roll)
            num_rolls_p2 += 1

    if not removable_rolls:
        break

    for roll in removable_rolls:
        del paper_map[roll]

end_time = timer()

print(num_rolls_p1)
print(num_rolls_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
