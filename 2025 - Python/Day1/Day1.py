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

dial_value = 50
password_old, password_new = 0, 0

for rotation in rotations:
    rotation_dist = int(rotation[1:])
    rotation_dist_rem = rotation_dist%100
    zero_crossings = rotation_dist//100

    if rotation[0]=='L':
        extra_zero_crossing = 1 if dial_value<rotation_dist_rem and dial_value!=0 else 0 
        dial_value = (dial_value - rotation_dist)%100
    else:
        extra_zero_crossing = abs(dial_value + rotation_dist_rem - 1)//100
        dial_value = (dial_value + rotation_dist)%100
    
    password_new += zero_crossings + extra_zero_crossing

    if dial_value==0:
        password_old += 1
        password_new += 1

end_time = timer()

print(password_old)
print(password_new)
print(f'Time elapsed: {end_time - start_time:.6f} s')
