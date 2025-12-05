from timeit import default_timer as timer

start_time = timer()

DAY_NUMBER = 5
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    ingredient_data = [line.strip() for line in file]

ranges_flag = 1
ranges = []
num_fresh_ingredients = 0

for line in ingredient_data:
    if line=='':
        ranges_flag = 0
        continue

    if ranges_flag==1:
        ranges.append(list(map(int, line.split('-'))))
    else:
        ingredient_ID = int(line)
        for min_range, max_range in ranges:
            if ingredient_ID>=min_range and ingredient_ID<=max_range:
                num_fresh_ingredients += 1
                break



end_time = timer()

print(num_fresh_ingredients)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
