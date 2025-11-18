from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 1
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    data = [line.strip() for line in file]

data.append('')

max_calories = [0,0,0]
current_calories = 0

for calories in data:
    if calories is not '':
        current_calories += int(calories)
    elif current_calories > max_calories[0]:
        max_calories[2] = max_calories[1]
        max_calories[1] = max_calories[0]
        max_calories[0] = current_calories
        current_calories = 0
    elif current_calories > max_calories[1]:
        max_calories[2] = max_calories[1]
        max_calories[1] = current_calories
        current_calories = 0
    elif current_calories > max_calories[2]:
        max_calories[2] = current_calories
        current_calories = 0
    else:
        current_calories = 0

end_time_1 = timer()

print(max_calories[0])
print(sum(max_calories))
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
