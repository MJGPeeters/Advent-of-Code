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
num_fresh_ingredients_total, num_fresh_ingredients_available = 0, 0

for line in ingredient_data:
    if line=='':
        ranges_flag = 0
        continue

    if ranges_flag==1:
        tmp_min, tmp_max = map(int, line.split('-'))
        removable_ranges = []
        contained = 0

        if not ranges:
            ranges = [[tmp_min, tmp_max]]
            continue

        for min_range, max_range in ranges:
            if min_range<=tmp_min<=max_range and min_range<=tmp_max<=max_range:
                contained = 1
                break                   
            elif min_range<tmp_min and tmp_min<=max_range<=tmp_max:
                tmp_min = min_range
                removable_ranges.append([min_range, max_range])
            elif tmp_min<=min_range<=tmp_max and tmp_min<=max_range<=tmp_max:
                removable_ranges.append([min_range, max_range])
            elif tmp_min<=min_range<=tmp_max and max_range>tmp_max:
                tmp_max = max_range
                removable_ranges.append([min_range, max_range])

        if not contained:
            ranges = [x for x in ranges if x not in removable_ranges]
            ranges.append([tmp_min, tmp_max])
    else:
        ingredient_ID = int(line)

        for min_range, max_range in ranges:
            if ingredient_ID>=min_range and ingredient_ID<=max_range:
                num_fresh_ingredients_available += 1
                break

num_fresh_ingredients_total = sum(max_range - min_range + 1 for min_range, max_range in ranges)

end_time = timer()

print(num_fresh_ingredients_available)
print(num_fresh_ingredients_total)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
