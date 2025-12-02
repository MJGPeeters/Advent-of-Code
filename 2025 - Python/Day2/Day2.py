from timeit import default_timer as timer

start_time = timer()

DAY_NUMBER = 2
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

for line in open(FILE_NAME, 'r'):
    ID_ranges = line.strip().split(',')

invalid_ID_accum = 0

for ID_range in ID_ranges:
    start_ID, end_ID = ID_range.split('-')

    if len(start_ID)==len(end_ID) and len(start_ID)%2==1:
        continue

    for ID in range(int(start_ID), int(end_ID)+1):
        string_ID = str(ID)
        if string_ID[0:int(len(string_ID)/2)]==string_ID[int(len(string_ID)/2):]:
            invalid_ID_accum += ID

end_time = timer()

print(invalid_ID_accum)
print(f'Time elapsed: {end_time - start_time:.6f} s')
