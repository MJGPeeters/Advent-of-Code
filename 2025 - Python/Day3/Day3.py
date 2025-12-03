from timeit import default_timer as timer

start_time = timer()

DAY_NUMBER = 3
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    banks = [[int(x) for x in line.strip()] for line in file]

total_joltage_p1, total_joltage_p2 = 0, 0

for bank in banks:
    max_tens = max(bank[0:-1])
    idx_max_tens = bank.index(max_tens)

    max_ones = max(bank[idx_max_tens+1:])

    total_joltage_p1 += 10*max_tens + max_ones

for bank in banks:
    idx_max_i = -1
    for i in range(1,13):
        max_i = max(bank[idx_max_i+1:len(bank)-12+i])
        idx_max_i += 1 + bank[idx_max_i+1:].index(max_i)

        total_joltage_p2 += max_i * (10**(12-i))

end_time = timer()

print(total_joltage_p1)
print(total_joltage_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
