from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np

start_time_1 = timer()

DAY_NUMBER = 10
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    instructions = [line.strip() for line in file]

signal_strength_sum = 0
register = []
value = 1
image_array = np.zeros((6,40))

for instruction in instructions:
    if instruction[0]=='n':
        register.append(value)
    else:
        register.extend([value, value])
        value += int(instruction.split()[1])

    if len(register)>240:
        break

for check_cycle in [20, 60, 100, 140, 180, 220]:
    signal_strength_sum += check_cycle*register[check_cycle-1]

for i,sprite_pos in enumerate(register):
    row, pixel_number = i//40, i%40

    if pixel_number in {sprite_pos-1, sprite_pos, sprite_pos+1}:
        image_array[row,pixel_number] = 1
    
end_time_1 = timer()

plt.imshow(image_array)
plt.show()

print(signal_strength_sum)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
