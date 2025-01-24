from timeit import default_timer as timer

def flipflop(pulse_in, ff_status):
    """
    Determine state and output of flip-flop module
    """

    ff_status = (ff_status + 1) % 2 if pulse_in==0 else ff_status
    output = ff_status if pulse_in==0 else None

    return output, ff_status

def conjunction(input_module, pulse_in, input_modules, memory):
    """
    Determine memory and output of conjunction module
    """

    if len(input_modules)==1:
        memory = pulse_in
        output = 0 if memory==1 else 1
    else:
        for i, module in enumerate(input_modules):
            if module==input_module:
                memory[i] = pulse_in
        output = 0 if all(m==1 for m in memory) else 1

    return output, memory

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_20.txt'
INPUT_NAME = 'Inputs/Input_2023_20.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

module_dict = {}
origin_dict = {}
pulses_set, new_pulses_set = set(), set()
dest_module_list = []

# Add all modules with initializations to module_dict
for line in file_lines:
    orig_module, destinations = line.split(' -> ')
    destinations = tuple(destinations.split(', '))
    module_type = orig_module[0]

    if module_type=='&':
        module_dict[orig_module[1:]] = module_type, destinations, -1
    elif module_type=='%':
        module_dict[orig_module[1:]] = module_type, destinations, 0
    else:
        broadcast_destinations = destinations

    for next_module in destinations:
        dest_module_list.append(next_module)
        if next_module in origin_dict:
            origin_dict[next_module].append(orig_module[1:])
        else:
            origin_dict[next_module] = [orig_module[1:]]

# Initialize memory of conjuction modules correctly
for module, (module_type, dests, _) in module_dict.items():
    if module_type=='&':
        d = origin_dict[module]
        memory_init = 0 if len(d)==1 else [0 for _ in d]
        module_dict[module] = module_type, dests, memory_init

# Find output modules (the ones appearing in destinations but not in list of modules)
for dest_module in dest_module_list:
    if dest_module not in module_dict:
        module_dict[dest_module] = 'output', 0, 0

# Put initial state in list with previous states
state = []
for _, _, status in module_dict.values():
    tmp = status if isinstance(status, int) else tuple(status)
    state.append(tmp)
state = tuple(state)

previous_states = {state}

total_low_pulses, total_high_pulses = 0, 0

for num_presses in range(1, 1001):
    total_low_pulses += 1

    # Fill pulses_set with pulses from broadcaster
    for curr_module in broadcast_destinations:
        module_type, _, status = module_dict[curr_module]
        pulses_set.add((0, curr_module, 'broadcaster'))

    # For every pulse in the pulse_set, determine if it changes the status of a module
    # and/or results in a new pulse that will be sent
    while pulses_set:
        total_low_pulses += sum(1 for pulse, _, _ in pulses_set if pulse==0)
        total_high_pulses +=sum(1 for pulse, _, _ in pulses_set if pulse==1)

        for pulse, curr_module, prev_module in pulses_set:
            module_type, destinations, curr_status = module_dict[curr_module]

            # Sent pulse through module, update status and get output pulse
            if module_type=='%':
                next_pulse, next_status = flipflop(pulse, curr_status)
            elif module_type=='&':
                module_inputs = origin_dict[curr_module]
                next_pulse, next_status = conjunction(prev_module, pulse, module_inputs, curr_status)
            else:
                module_type = 'output'
                destinations = pulse
                next_status = 0
                next_pulse = None

            # Update status of module
            module_dict[curr_module] = module_type, destinations, next_status

            # If there is a pulse output, add it to new_pulses_set
            if next_pulse is not None:
                for next_module in destinations:
                    new_pulses_set.add((next_pulse, next_module, curr_module))

        pulses_set = new_pulses_set
        new_pulses_set = set()

    state = []
    for _, _, status in module_dict.values():
        tmp = status if isinstance(status, int) else tuple(status)
        state.append(tmp)
    state = tuple(state)

    if state in previous_states:
        break

    previous_states.add(state)

ans1 = int((total_low_pulses * total_high_pulses) * (1000 / num_presses)**2)

end_time_1 = timer()

print(ans1)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# # Part II

# start_time_2 = timer()

# ans2 = 0



# end_time_2 = timer()

# print(ans2)
# print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')
