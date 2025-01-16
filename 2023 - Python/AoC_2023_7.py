from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_7.txt'
inputName = 'Inputs/Input_2023_7.txt'

with open(inputName, "r") as file:
    fileContent = file.read()

fileLines = fileContent.splitlines()

FiOAK, FoOAK, FH, ThOAK, TP, OP, HC = [], [], [], [], [], [], []

for line in fileLines:
    hand, bid = tuple(line.split())

    counts = dict()
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    counts = sorted([*counts.values()], reverse=True)
    counts = counts[0:2]

    origCards = 'AKQJT'
    sortCards = 'FEDCB'
    mytable = str.maketrans(origCards, sortCards)
    newHand = hand.translate(mytable)

    comb = [newHand, bid]

    if counts[0]==5:
        FiOAK.append(comb)
    elif counts[0:2]==[4,1]:
        FoOAK.append(comb)
    elif counts[0:2]==[3,2]:
        FH.append(comb)
    elif counts[0:2]==[3,1]:
        ThOAK.append(comb)
    elif counts[0:2]==[2,2]:
        TP.append(comb)
    elif counts[0:2]==[2,1]:
        OP.append(comb)
    else:
        HC.append(comb)

handTypes = [HC, OP, TP, ThOAK, FH, FoOAK, FiOAK]

baseRank = 1
winnings = 0

for handType in handTypes:
    sortedHands = sorted(handType)
    winnings += sum([(rank + baseRank)*int(bid) for rank, (hand, bid) in enumerate(sortedHands)])
    baseRank += len(handType)

endTime1 = timer()

print(winnings)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II
startTime2 = timer()

sum2 = 0

# Every hand with at least one J in it has to be checked
FiOAK, FoOAK, FH, ThOAK, TP, OP, HC = [], [], [], [], [], [], []

for line in fileLines:
    hand, bid = tuple(line.split())

    counts = dict()
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    counts = sorted([*counts.values()], reverse=True)
    counts = counts[0:2]

    origCards = 'AKQJT'
    sortCards = 'FED0B'
    mytable = str.maketrans(origCards, sortCards)
    newHand = hand.translate(mytable)

    comb = [newHand, bid]
    numJacks = newHand.count('0')

    if counts[0]==5:
        FiOAK.append(comb)
    elif counts[0:2]==[4,1]:
        if numJacks==1 or numJacks==4:
            FiOAK.append(comb)
        else:
            FoOAK.append(comb)
    elif counts[0:2]==[3,2]:
        if numJacks==2 or numJacks==3:
            FiOAK.append(comb)
        else:
            FH.append(comb)
    elif counts[0:2]==[3,1]:
        if numJacks==1 or numJacks==3:
            FoOAK.append(comb)
        else:
            ThOAK.append(comb)
    elif counts[0:2]==[2,2]:
        if numJacks==1:
            FH.append(comb)
        elif numJacks==2:
            FoOAK.append(comb)
        else:
            TP.append(comb)
    elif counts[0:2]==[2,1]:
        if numJacks==1 or numJacks==2:
            ThOAK.append(comb)
        else:
            OP.append(comb)
    else:
        if numJacks==1:
            OP.append(comb)
        else:
            HC.append(comb)

handTypes = [HC, OP, TP, ThOAK, FH, FoOAK, FiOAK]

baseRank = 1
winnings = 0

for handType in handTypes:
    sortedHands = sorted(handType)
    winnings += sum([(rank + baseRank)*int(bid) for rank, (hand, bid) in enumerate(sortedHands)])
    baseRank += len(handType)

endTime2 = timer()

print(winnings)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))