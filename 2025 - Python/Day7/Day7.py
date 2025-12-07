from timeit import default_timer as timer

start_time = timer()

DAY_NUMBER = 7
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

split_count = 0

for line_number, line in enumerate(open(FILE_NAME, 'r')):
    if line_number==0:
        tachyons = {line.find('S')}
        continue
    elif line_number%2==1:
        continue

    splitters = (idx for idx, x in enumerate(line) if x=='^')

    for splitter in splitters:
        if splitter in tachyons:
            tachyons.remove(splitter)
            tachyons.add(splitter-1)
            tachyons.add(splitter+1)
            split_count += 1

end_time = timer()

print(split_count)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
