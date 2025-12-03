from timeit import default_timer as timer

def max_joltage(input_banks, num_batteries):
    total_joltage = 0
    
    for bank in input_banks:
        idx = 0
        for n in range(num_batteries-1,-1,-1):
            max_battery = max(bank[idx:len(bank)-n])
            idx += 1 + bank[idx:].index(max_battery)

            total_joltage += max_battery * (10**n)

    return total_joltage

start_time = timer()

DAY_NUMBER = 3
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    banks = [[int(x) for x in line.strip()] for line in file]

total_joltage_p1 = max_joltage(banks, 2)
total_joltage_p2 = max_joltage(banks, 12)

end_time = timer()

print(total_joltage_p1)
print(total_joltage_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
