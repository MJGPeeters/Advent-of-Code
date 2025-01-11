with open("Input/Input_2023_1.txt", "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

sum1 = 0
sum2 = 0

numLongList  = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numShortList = ['1','2','3','4','5','6','7','8','9']

for fileLine in fileLines:
    tmp1 = [character for character in fileLine if character.isdigit()]
    sum1 += int(tmp1[0] + tmp1[-1])

    idx = []

    for numLong in numLongList:
        idx = [idx, fileLine.find(numLong)]




    tmp = fileLine.find(numLongList)

    # tmp2 = [character for character in fileLine if character in numShortList or character in numLongList]

    # for index, dummy in enumerate(fileLine):
    #     tmp2 = [numShortList[index] for numLongList[index] in fileLine]
    
    # print(tmp2)






print(sum1)
print(sum2)