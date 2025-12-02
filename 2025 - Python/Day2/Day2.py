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

prime_factors = {2:(1,), 3:(1,), 4:(1,2), 5:(1,), 6:(1,2,3), 7:(1,), 8:(1,2,4), 9:(1,3), 10:(1,2,5)}
invalid_ID_accum_1, invalid_ID_accum_2 = 0, 0

for ID_range in ID_ranges:
    start_ID, end_ID = ID_range.split('-')

    ID_lengths = [i for i in range(len(start_ID), len(end_ID) + 1) if i>1]
    invalid_IDs = set()

    for ID_length in ID_lengths:
        for sequence_length in prime_factors[ID_length]:
            for sub_sequence in range(10**(sequence_length-1),10**sequence_length):
                test_ID = int(str(sub_sequence)*int(ID_length/sequence_length))
                if test_ID<=int(end_ID) and test_ID>=int(start_ID) and test_ID not in invalid_IDs:
                    string_ID = str(test_ID)
                    if string_ID[0:int(len(string_ID)/2)]==string_ID[int(len(string_ID)/2):]:
                        invalid_ID_accum_1 += test_ID                    
                    invalid_IDs.add(test_ID)
                    invalid_ID_accum_2 += test_ID

end_time = timer()

print(invalid_ID_accum_1)
print(invalid_ID_accum_2)
print(f'Time elapsed: {end_time - start_time:.6f} s')
