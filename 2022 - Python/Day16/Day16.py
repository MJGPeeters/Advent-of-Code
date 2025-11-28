from timeit import default_timer as timer

def valve_step(valve_dict, valve_name, valve_status, cache_dict, time_step=0, max_time=30):
    flow_rate, tunnels = valve_dict[valve_name]
    
    if valve_name in flow_dict:
        flow_idx = flow_dict[valve_name]
        status = valve_status[flow_idx]
    else:
        status = 0

    pressure_list = []

    if (valve_status, valve_name) in cache_dict:
        return 0

    time_step += 1

    if time_step==max_time:
        return 0

    cache_dict[(valve_status, valve_name)] = time_step

    # If applicable, open valve
    if status==0 and flow_rate>0:
        valve_status = valve_status[:flow_idx] + (1,) + valve_status[flow_idx+1:]
        added_pressure = flow_rate*(max_time - time_step + 1)
        tmp_pressure = valve_step(valve_dict, valve_name, valve_status, cache_dict, time_step, max_time)
        pressure_list.append(tmp_pressure + added_pressure)

    # Check all the tunnels
    for tunnel in tunnels:
        tmp_pressure = valve_step(valve_dict, tunnel, valve_status, cache_dict, time_step, max_time)
        pressure_list.append(tmp_pressure)

    # See which option results in the highest max pressure released
    max_pressure_released = max(pressure_list)

    return max_pressure_released

start_time = timer()

DAY_NUMBER = 16
TEST = True

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    valve_details = [line.strip().split() for line in file]

max_pressure = 0
valves, flow_dict = {}, {}
tmp_idx = 0

for valve_detail in valve_details:
    valve_name = valve_detail[1]
    tmp_flow_rate = valve_detail[4].split('=')
    valve_flow_rate = int(tmp_flow_rate[1][0:-1])

    if valve_flow_rate>0:
        flow_dict[valve_name] = tmp_idx
        tmp_idx += 1
    
    valve_tunnels = []
    for i in range(9,len(valve_detail)):
        if i==len(valve_detail)-1:
            valve_tunnels.append(valve_detail[i])
        else:
            valve_tunnels.append(valve_detail[i][0:-1])

    valves[valve_name] = [valve_flow_rate, valve_tunnels]

valve_status = tuple(0 for _ in flow_dict)

max_pressure = valve_step(valves, 'AA', valve_status, {}, 0, 30)

end_time = timer()

print(max_pressure)
print(f'Time elapsed: {end_time - start_time:.6f} s')
