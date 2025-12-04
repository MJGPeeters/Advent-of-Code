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
to_be_removed, to_be_checked = set(), set()
num_rolls_p1 = 0

for roll in paper_map:
    if sum(neighbor+roll in paper_map for neighbor in neighbors)<4:
        to_be_removed.add(roll)
        if roll in to_be_checked:
            to_be_checked.remove(roll)
        to_be_checked.update(roll+neighbor for neighbor in neighbors if (roll+neighbor in paper_map and roll+neighbor not in to_be_removed))
        num_rolls_p1 += 1

num_rolls_p2 = num_rolls_p1

while to_be_checked:
    for roll in to_be_removed:
        del paper_map[roll]
    to_be_removed, to_be_checked_new = set(), set()

    for roll in to_be_checked:
        if sum(neighbor+roll in paper_map for neighbor in neighbors)<4:
            to_be_removed.add(roll)
            if roll in to_be_checked_new:
                to_be_checked_new.remove(roll)
            to_be_checked_new.update(roll+neighbor for neighbor in neighbors if (roll+neighbor in paper_map and roll+neighbor not in to_be_removed))
            num_rolls_p2 += 1

    to_be_checked = to_be_checked_new

end_time = timer()

print(num_rolls_p1)
print(num_rolls_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
