from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_2.txt'
inputName = 'Inputs/Input_2023_2.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

sum1 = 0

numRed = 12
numGreen = 13
numBlue = 14

# Part I
for fileLine in fileLines:
    idPart, gamePart = fileLine.split(':')
    gameID = int(idPart[5:])

    grabs = gamePart.split(';')
    possible = 1

    for grab in grabs:
        if not possible:
            break

        cubesList = grab.split(',')
        
        for cubes in cubesList:
            tmp = cubes.split(' ')
            numCubes = int(tmp[1])
            colorCubes = tmp[2]

            if colorCubes=='red' and numCubes>numRed:
                possible = 0
                break
            elif colorCubes=='green' and numCubes>numGreen:
                possible = 0
                break
            elif colorCubes=='blue' and numCubes>numBlue:
                possible = 0
                break

    if possible:
        sum1 += gameID

endTime1 = timer()

print(sum1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II

startTime2 = timer()
sum2 = 0

for fileLine in fileLines:
    idPart, gamePart = fileLine.split(':')
    gameID = int(idPart[5:])

    grabs = gamePart.split(';')
    possible = 1

    minRed = 0
    minGreen = 0
    minBlue = 0

    for grab in grabs:
        cubesList = grab.split(',')
        
        for cubes in cubesList:
            tmp = cubes.split(' ')
            numCubes = int(tmp[1])
            colorCubes = tmp[2]

            if colorCubes=='red' and numCubes>minRed:
                minRed = numCubes
            elif colorCubes=='green' and numCubes>minGreen:
                minGreen = numCubes
            elif colorCubes=='blue' and numCubes>minBlue:
                minBlue = numCubes

    sum2 += minRed*minGreen*minBlue

endTime2 = timer()

print(sum2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))