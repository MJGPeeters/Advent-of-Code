from timeit import default_timer as timer
from sortedcontainers import SortedDict
import math as m

start_time = timer()

DAY_NUMBER = 8
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
    num_connections = 10
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"
    num_connections = 1000

with open(FILE_NAME, 'r') as file:
    junctions = [tuple(int(pos) for pos in line.strip().split(',')) for line in file]

shortest_distances = SortedDict()
for i in range(num_connections):
    shortest_distances[10**6 - i] = 0
max_distance = 10**6

for idx_junction, junction in enumerate(junctions):
    for i in range(idx_junction+1,len(junctions)):
        distance = m.sqrt((junction[0] - junctions[i][0])**2 + (junction[1] - junctions[i][1])**2 + (junction[2] - junctions[i][2])**2)
        if distance<max_distance:
            if distance in shortest_distances:
                shortest_distances[distance].add(idx_junction, i)
            else:
                shortest_distances[distance] = {idx_junction, i}

            shortest_distances.popitem()
            max_distance = shortest_distances.peekitem()[0]

first_circuit = shortest_distances.popitem(0)[1]
circuits = [first_circuit]

for k in shortest_distances:
    jb1, jb2 = shortest_distances[k]

    new_circuit_flag = 1
    jb1_flag, jb2_flag = -1, -1

    for idx_circuit, circuit in enumerate(circuits):
        if jb1 in circuit and jb2 in circuit:
            new_circuit_flag = 0
            continue
        elif jb1 in circuit:
            jb1_flag = idx_circuit
            circuit.add(jb2)
            new_circuit_flag = 0
        elif jb2 in circuit:
            jb2_flag = idx_circuit
            circuit.add(jb1)
            new_circuit_flag = 0

    if jb1_flag>-1 and jb2_flag>-1:
        circuits[jb1_flag].update(circuits[jb2_flag])
        circuits.pop(jb2_flag)
        
    if new_circuit_flag:
        circuits.append({jb1, jb2})

circuit_sizes = [len(c) for c in circuits]
circuit_sizes.sort(reverse=True)

circuit_product = circuit_sizes[0]*circuit_sizes[1]*circuit_sizes[2]

end_time = timer()

print(circuit_product)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
