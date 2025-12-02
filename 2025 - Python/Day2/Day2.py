from timeit import default_timer as timer
import math as m

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

invalid_ID_accum_p1, invalid_ID_accum_p2 = 0, 0

for ID_range in ID_ranges:
    start_ID, end_ID = map(int, ID_range.split('-'))

    ID_lengths = [i for i in range(len(str(start_ID)), len(str(end_ID)) + 1) if i>1]
    invalid_IDs = set()

    for length_idx, ID_length in enumerate(ID_lengths):
        for sequence_length in prime_factors[ID_length]:
            if len(ID_lengths)==1:
                sub_sequence_start = start_ID//10**(ID_length-sequence_length)
                sub_sequence_end = end_ID//10**(ID_length-sequence_length)
            elif length_idx==0:
                sub_sequence_start = start_ID//10**(ID_length-sequence_length)
                sub_sequence_end = 10**sequence_length - 1
            else:
                sub_sequence_start = 10**(sequence_length-1)
                sub_sequence_end = end_ID//10**(ID_length-sequence_length)

            for sub_sequence in range(sub_sequence_start,sub_sequence_end+1):
                test_ID = int(str(sub_sequence)*int(ID_length/sequence_length))

                if test_ID<=end_ID and test_ID>=start_ID and test_ID not in invalid_IDs:
                    if test_ID//10**int(ID_length/2)==test_ID%10**int(ID_length/2):
                        invalid_ID_accum_p1 += test_ID 

                    invalid_IDs.add(test_ID)
                    invalid_ID_accum_p2 += test_ID

end_time = timer()

print(invalid_ID_accum_p1)
print(invalid_ID_accum_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
