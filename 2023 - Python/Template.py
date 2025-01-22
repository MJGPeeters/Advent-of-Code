from timeit import default_timer as timer

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_13.txt'
INPUT_NAME = 'Inputs/Input_2023_13.txt'

with open(INPUT_NAME, "r") as file:
    fileLines = file.read().splitlines()

ans1 = 0



end_time_1 = timer()

print(ans1)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# # Part II

# start_time_2 = timer()

# ans2 = 0



# end_time_2 = timer()

# print(ans2)
# print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
