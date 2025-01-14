from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_5.txt'
inputName = 'Inputs/Input_2023_5.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

sum1 = 0
plans = []
planIdx = -1

# Make list of seeds and arrays for the different plans, in the format [source_begin, source_end, diff]
for line in fileLines:
    splitLine = line.split()
    if splitLine==[]:
        plans.append([])
        planIdx += 1
    elif splitLine[0]=='seeds:':
        seeds = [int(seed) for seed in splitLine if seed.isdigit()]
    elif splitLine[0].isdigit():
        x = [int(splitLine[1]), int(splitLine[1]) + int(splitLine[2]), int(splitLine[0]) - int(splitLine[1])]
        plans[planIdx].append(x)
 
minLocation = 10**10

for seed in seeds:
    number = seed
    for plan in plans:
        for scope in plan:
            if scope[0]<=number<scope[1]:
                number += scope[2]
                break
    
    if number<minLocation:
        minLocation = number

endTime1 = timer()

print(minLocation)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# # Part II

# startTime2 = timer()

# sum2 = 0


    
# sum2 = sum(numCards)

# endTime2 = timer()

# print(sum2)
# print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))