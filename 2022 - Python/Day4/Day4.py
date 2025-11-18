from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 4
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

pair_list = []

with open(FILE_NAME, 'r') as file:
    for line in file:
        pair = line[0:-1].split(',')
        pair_list.append([pair[0].split('-'),pair[1].split('-')])

contain_count = 0
overlap_count = 0

for pair in pair_list:
    min_one, max_one = int(pair[0][0]), int(pair[0][1])
    min_two, max_two = int(pair[1][0]), int(pair[1][1])

    len_one = max_one - min_one + 1
    len_two = max_two - min_two + 1

    if len_one==len_two and min_one==min_two:
        contain_count += 1
    elif len_one<len_two and min_one>=min_two and max_one<=max_two:
        contain_count += 1
    elif len_one>len_two and min_one<=min_two and max_one>=max_two:
        contain_count += 1
    
    if min_one<min_two and max_one>=min_two:
        overlap_count += 1
    elif min_one>=min_two and min_one<=max_two:
        overlap_count +=1
        
end_time_1 = timer()

print(contain_count)
print(overlap_count)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
