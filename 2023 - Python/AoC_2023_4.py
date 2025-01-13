from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_4.txt'
inputName = 'Inputs/Input_2023_4.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

sum1 = 0

for line in fileLines:
    winningNums, yourNums = line.split(':')[1].split('|')

    winningNums = [int(n) for n in winningNums.split()]
    yourNums = [int(n) for n in yourNums.split()]

    n = sum([1 for num in yourNums if num in winningNums])

    if n>0:
        sum1 += 2**(n-1)

endTime1 = timer()

print(sum1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

startTime2 = timer()

numCards = [1]*len(fileLines)
sum2 = 0

for lineNumber, line in enumerate(fileLines):
    winningNums, yourNums = line.split(':')[1].split('|')

    winningNums = [int(n) for n in winningNums.split()]
    yourNums = [int(n) for n in yourNums.split()]

    n = sum([1 for num in yourNums if num in winningNums])

    for i in range(lineNumber + 1, lineNumber + n + 1):
        numCards[i] += numCards[lineNumber]
    
sum2 = sum(numCards)

endTime2 = timer()

print(sum2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))