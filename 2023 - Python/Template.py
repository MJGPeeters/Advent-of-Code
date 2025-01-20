from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_13.txt'
inputName = 'Inputs/Input_2023_13.txt'

with open(inputName, "r") as file:
    fileLines = file.read().splitlines()

ans1 = 0



endTime1 = timer()

print(ans1)
print(f'Time elapsed: {endTime1 - startTime1:.6f} s')

# # Part II

# startTime2 = timer()

# ans2 = 0



# endTime2 = timer()

# print(ans2)
# print(f'Time elapsed: {endTime2 - startTime2:.6f} s')
