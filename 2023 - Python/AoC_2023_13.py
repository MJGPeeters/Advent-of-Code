from timeit import default_timer as timer
import numpy as np

startTime1 = timer()

testName = 'Tests/Test_2023_13.txt'
inputName = 'Inputs/Input_2023_13.txt'

with open(inputName, "r") as file:
    fileLines = file.read().splitlines()

ans1 = 0

patterns = []
pattern = []

for line in fileLines:
    if line=='':
        patterns.append(np.array(pattern))
        pattern = []
        continue
    pattern.append([1 if char=='#' else -1 for char in line])
patterns.append(np.array(pattern))

for pattern in patterns:
    numRows, numCols = np.shape(pattern)
    flag = 0

    # Check horizontal reflections
    for rowNum in range(1,numRows):
        checkPattern = pattern[:rowNum*2,:] if rowNum<(numRows / 2) else pattern[2*rowNum - numRows:,:]
        flipCheckPattern = np.flipud(checkPattern)
        mPattern = np.multiply(checkPattern, flipCheckPattern)
        if (mPattern>0).all():
            ans1 += rowNum * 100
            flag = 1
            break
    
    if flag:
        continue

    # Check vertical reflections
    for colNum in range(1,numCols):
        checkPattern = pattern[:,:colNum*2] if colNum<(numCols / 2) else pattern[:,2*colNum - numCols:]
        flipCheckPattern = np.fliplr(checkPattern)
        mPattern = np.multiply(checkPattern, flipCheckPattern)
        if (mPattern>0).all():
            ans1 += colNum
            break
    
endTime1 = timer()

print(ans1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

startTime2 = timer()

ans2 = 0

for pattern in patterns:
    numRows, numCols = np.shape(pattern)
    flag = 0

    # Check horizontal reflections
    for rowNum in range(1,numRows):
        checkPattern = pattern[:rowNum*2,:] if rowNum<(numRows / 2) else pattern[2*rowNum - numRows:,:]
        flipCheckPattern = np.flipud(checkPattern)
        mPattern = np.multiply(checkPattern, flipCheckPattern)
        if sum(sum(mPattern<0))==2:
            ans2 += rowNum * 100
            flag = 1
            break
    
    if flag:
        continue

    # Check vertical reflections
    for colNum in range(1,numCols):
        checkPattern = pattern[:,:colNum*2] if colNum<(numCols / 2) else pattern[:,2*colNum - numCols:]
        flipCheckPattern = np.fliplr(checkPattern)
        mPattern = np.multiply(checkPattern, flipCheckPattern)
        if sum(sum(mPattern<0))==2:
            ans2 += colNum
            break

endTime2 = timer()

print(ans2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
