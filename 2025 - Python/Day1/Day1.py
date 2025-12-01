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

dial_value, password = 50, 0

for rotation in rotations:
    if rotation[0]=='L':
        dial_value = (dial_value - int(rotation[1:]))%100
    else:
        dial_value = (dial_value + int(rotation[1:]))%100
    
    if dial_value==0:
        password += 1

end_time = timer()

print(password)
print(f'Time elapsed: {end_time - start_time:.6f} s')
