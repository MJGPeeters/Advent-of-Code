from timeit import default_timer as timer
import math as m

startTime1 = timer()

testName = 'Tests/Test_2023_6.txt'
inputName = 'Inputs/Input_2023_6.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

races = []

for line in fileLines:
    tmpList = [int(x) for x in line.split() if x.isdigit()]
    races.append(tmpList)

numWays = 1

for i in range(len(races[0])):
    time = races[0][i]
    distance = races[1][i]

    minTime = m.floor((time - m.sqrt(time**2 - 4*distance))/2) + 1
    numTimes = time + 1 - 2*minTime

    numWays = numWays * numTimes

endTime1 = timer()

print(numWays)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II
startTime2 = timer()

time, distance = 46828479, 347152214061471
print(time + 1 - 2*(m.floor((time - m.sqrt(time**2 - 4*distance))/2) + 1))

endTime2 = timer()

print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))