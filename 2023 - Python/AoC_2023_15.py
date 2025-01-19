from timeit import default_timer as timer

startTime1 = timer()

testName = 'Tests/Test_2023_15.txt'
inputName = 'Inputs/Input_2023_15.txt'

with open(inputName, "r") as file:
    steps = file.read().split(',')

def aoc_hash(string):
    """
    Compute AoC hash value for input string
    """

    value = 0

    for char in string:
        value += ord(char)
        value = (value * 17) % 256
    
    return value

ans1 = 0

for step in steps:
    ans1 += aoc_hash(step)

endTime1 = timer()

print(ans1)
print('Time elapsed: {:.6f} s'.format(endTime1 - startTime1))

# Part II
startTime2 = timer()

ans2 = 0

boxes = [[] for i in range(256)]

for step in steps:
    if '=' in step:
        stepLabel = step[:-2]
        stepLabelHash = aoc_hash(stepLabel)
        focalLength = int(step[-1])

        if not boxes[stepLabelHash]:
            boxes[stepLabelHash] = [[stepLabel, focalLength]]
            continue

        tmp = [index for index, (label, fL)  in enumerate(boxes[stepLabelHash]) if label==stepLabel]

        if not tmp:
            boxes[stepLabelHash].append([stepLabel, focalLength])
        else:
            boxes[stepLabelHash][tmp[0]][1] = focalLength

    else:
        stepLabel = step[:-1]
        stepLabelHash = aoc_hash(stepLabel)

        if not boxes[stepLabelHash]:
            continue

        tmp = [index for index, (label, fL)  in enumerate(boxes[stepLabelHash]) if label==stepLabel]

        if not tmp:
            continue
        else:
            del boxes[stepLabelHash][tmp[0]]

for boxIndex, box in enumerate(boxes):
    ans2 += sum([(boxIndex + 1) * (slotNumber + 1) * slot[1] for slotNumber, slot in enumerate(box)])

endTime2 = timer()

print(ans2)
print('Time elapsed: {:.6f} s'.format(endTime2 - startTime2))
