from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 11
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    notes = [line.strip() for line in file]

monkey_dict = {}
items_dict = {}

if TEST:
    inspection_numbers = [0,0,0,0]
else:
    inspection_numbers = [0,0,0,0,0,0,0,0]

for line in notes:
    if line=='':
        continue
    
    split_line = line.split()
    
    if line[0]=='M':
        tmp_monkey_number = int(line[-2])
    elif line[0]=='S':
        tmp_items = line.split(':')[1].split(',')
        items_dict[tmp_monkey_number] = [int(item) for item in tmp_items]
    elif line[0]=='O':
        if split_line[-1]=='old':
            monkey_dict[tmp_monkey_number] = ['^', 2]
        else:
            monkey_dict[tmp_monkey_number] = [split_line[-2], int(split_line[-1])]
    elif line[0]=='T':
        monkey_dict[tmp_monkey_number].append(int(split_line[-1]))
    elif line[0]=='I':
        monkey_dict[tmp_monkey_number].append(int(split_line[-1]))

for _ in range(20):
    for monkey_number in range(len(monkey_dict)):
        items = items_dict[monkey_number]
        properties = monkey_dict[monkey_number]

        operation = properties[0]
        operand = properties[1]
        test = properties[2]
        true_monkey = properties[3]
        false_monkey = properties[4]

        while items:
            inspection_numbers[monkey_number] += 1

            worry_level = items.pop(0)

            if operation=='*':
                worry_level = worry_level*operand
            elif operation=='+':
                worry_level += operand
            else:
                worry_level = worry_level**2

            worry_level = int(worry_level/3)

            if worry_level%test==0:
                items_dict[true_monkey].append(worry_level)
            else:
                items_dict[false_monkey].append(worry_level)

inspection_numbers.sort()
monkey_business = inspection_numbers[-1]*inspection_numbers[-2]

end_time_1 = timer()

print(monkey_business)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
