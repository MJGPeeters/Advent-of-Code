from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_11.txt'
inputName = 'Inputs/Input_2023_11.txt'

with open(inputName, "r") as file:
    galaxyMap = file.read().splitlines()

allRows, allCols = {row for row in range(len(galaxyMap))}, {col for col in range(len(galaxyMap))}
filledRows, filledCols = set(), set()
oldGalaxies, galaxies = [], []

for rowNumber, row in enumerate(galaxyMap):
    rowGalaxies = [[rowNumber, colNumber] for colNumber, c in enumerate(row) if c=='#']
    if rowGalaxies:
        filledRows.add(rowNumber)
        filledCols.update([col for row, col in rowGalaxies])
        oldGalaxies.append(rowGalaxies)

emptyRows, emptyCols = sorted(allRows - filledRows), sorted(allCols - filledCols)

# For every galaxy, add number of empty rows, columns smaller than coordinate to coordinates
for row in oldGalaxies:
    for r, c in row:
        padding = sum([1 for x in emptyCols if x<c])
        galaxies.append((r, c + padding))

# For every pair of galaxies, compute Manhattan distance, add to ans1
ans1 = sum([abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for i, g1 in enumerate(galaxies) for g2 in galaxies[i:]])

endTime1 = timer()

print(ans1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II
startTime2 = timer()

# For every galaxy, add number of empty rows, columns smaller than coordinate to coordinates
galaxies = []

for row in oldGalaxies:
    for r, c in row:
        padding = sum([10**6-1 for x in emptyCols if x<c])
        galaxies.append((r, c + padding))

# For every pair of galaxies, compute Manhattan distance, add to ans1
ans2 = sum([abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for i, g1 in enumerate(galaxies) for g2 in galaxies[i:]])

endTime2 = timer()

print(ans2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))