from timeit import default_timer as timer

def remove_paper_rolls(to_be_removed, to_be_checked, paper_map_dict):
    for roll in to_be_removed:
        del paper_map[roll]

    neighbors = {1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j}
    to_be_removed, to_be_checked_next = set(), set()
    num_rolls = 0

    for roll in to_be_checked:
        if sum(neighbor+roll in paper_map_dict for neighbor in neighbors)<4:
            to_be_removed.add(roll)
            if roll in to_be_checked_next:
                to_be_checked_next.remove(roll)
            to_be_checked_next.update(roll+neighbor for neighbor in neighbors if (roll+neighbor in paper_map and roll+neighbor not in to_be_removed))
            num_rolls += 1

    return to_be_removed, to_be_checked_next, num_rolls

start_time = timer()

DAY_NUMBER = 4
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    paper_map = {complex(row,col):1 for row, line in enumerate(file) for col, element in enumerate(line) if element=='@'}

to_be_removed, to_be_checked = set(), paper_map
num_rolls_p1, num_rolls_p2 = 0, 0

while to_be_checked:
    to_be_removed, to_be_checked, num_removed_rolls = remove_paper_rolls(to_be_removed, to_be_checked, paper_map)

    if num_rolls_p1==0:
        num_rolls_p1 = num_removed_rolls

    num_rolls_p2 += num_removed_rolls

end_time = timer()

print(num_rolls_p1)
print(num_rolls_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
