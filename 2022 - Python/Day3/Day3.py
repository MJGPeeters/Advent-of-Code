from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 3
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    rucksacks = [line.split() for line in file]

sum_priorities = 0

for rucksack in rucksacks:
    contents = rucksack[0]
    compartment_size = int(len(contents)/2)
    for element in contents[0:compartment_size]:
        if element in contents[compartment_size:]:
            if element.isupper():
                sum_priorities += ord(element) - 38
            else:
                sum_priorities += ord(element) - 96
            break

sum_priorities_badges = 0

for group in range(0,int(len(rucksacks)/3)):
    rucksack_group = [rucksacks[3*group], rucksacks[3*group+1], rucksacks[3*group+2]]
    for element in rucksack_group[0][0]:
        if element in rucksack_group[1][0]:
            if element in rucksack_group[2][0]:
                if element.isupper():
                    sum_priorities_badges += ord(element) - 38
                else:
                    sum_priorities_badges += ord(element) - 96
                break   

end_time_1 = timer()

print(sum_priorities)
print(sum_priorities_badges)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
