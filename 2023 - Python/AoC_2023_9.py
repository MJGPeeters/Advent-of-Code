from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_9.txt'
inputName = 'Inputs/Input_2023_9.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

sum1 = 0

for line in fileLines:
    nums = [x for x in map(int, line.split())]
    nextValue = nums[-1]

    while nums.count(nums[0])!=len(nums): 
        nums = [a - b for a, b in zip(nums[1:], nums[:-1])]
        nextValue += nums[-1]
    
    sum1 += nextValue

endTime1 = timer()

print(sum1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

startTime2 = timer()

numCards = [1]*len(fileLines)
sum2 = 0

for line in fileLines:
    nums = [x for x in map(int, line.split())]
    firstValues = [nums[0]]

    while nums.count(nums[0])!=len(nums): 
        nums = [a - b for a, b in zip(nums[1:], nums[:-1])]
        firstValues.append(nums[0])

    previousValue = firstValues[-1] 
    for x in firstValues[-2::-1]:
        previousValue = x - previousValue

    sum2 += previousValue

endTime2 = timer()

print(sum2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))