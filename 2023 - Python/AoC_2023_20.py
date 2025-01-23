from timeit import default_timer as timer

def flipflop(pulse_in, status=0):
    """
    Determine state of flip-flop module
    """

    status = (status + 1) % 2 if pulse_in==0 else status

    return status

def conjunction(pulse_in_1, pulse_in_2, memory=(0, 0)):
    """
    Determine memory and output of conjunction module
    """

    memory_1, memory_2 = memory

    memory_1 = pulse_in_1 if pulse_in_1 is not None else memory_1
    memory_2 = pulse_in_2 if pulse_in_2 is not None else memory_2

    output = 1 if memory_1==1 and memory_2==1 else 0

    return output, (memory_1, memory_2)

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_20.txt'
INPUT_NAME = 'Inputs/Input_2023_20.txt'

with open(TEST_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

module_dict = {}

for line in file_lines:
    module, destinations = line.split(' -> ')
    destinations = tuple(destinations.split(', '))
    module_type = module[0]

    if module_type=='b':
        module_dict[module] = destinations
    elif module_type=='%':
        module_dict[module[1:]] = module_type, destinations, 0, None
    else:
        module_dict[module[1:]] = module_type, destinations, (0, 0), None

for dest in module_dict['broadcaster']:
    module_type, destinations, status, input = module_dict[dest]

    status = flipflop(0, status)

    module_dict[dest] = module_type, destinations, status, None

while pulses:
    for pulse in pulses:



end_time_1 = timer()

print(0)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# # Part II

# start_time_2 = timer()

# ans2 = 0



# end_time_2 = timer()

# print(ans2)
# print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
