from timeit import default_timer as timer

start_time = timer()

DAY_NUMBER = 1
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    rotations = [line.strip() for line in file]

dial_value, password_old, password_new = 50, 0, 0

for rotation in rotations:
    if rotation[0]=='L':
        dial_value = (dial_value - int(rotation[1:]))%100
    else:
        dial_value = (dial_value + int(rotation[1:]))%100
    
    if dial_value==0:
        password_old += 1

dial_value = 50

for rotation in rotations:
    if rotation[0]=='L':
        new_dial_value = dial_value - int(rotation[1:])
        if dial_value==0:
            password_new += abs(new_dial_value+1)//100
        elif new_dial_value<0:
            password_new += 1 + abs(new_dial_value+1)//100
    else:
        new_dial_value = dial_value + int(rotation[1:])
        if new_dial_value>99:
            password_new += abs(new_dial_value-1)//100
    
    dial_value = new_dial_value%100

    if dial_value==0:
        password_new += 1

end_time = timer()

print(password_old)
print(password_new)
print(f'Time elapsed: {end_time - start_time:.6f} s')
