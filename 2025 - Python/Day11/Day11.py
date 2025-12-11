from timeit import default_timer as timer
from functools import cache

@cache
def paths_to_out(input):
    next_devices = devices[input]
    num_paths = 0

    for device in next_devices:
        if device=='out':
            return 1
        
        num_paths += paths_to_out(device)        
    
    return num_paths

@cache
def paths_with_dac_fft(input):
    next_devices = devices[input]
    num_paths_none, num_paths_dac, num_paths_fft, num_paths_both = 0, 0, 0, 0

    for device in next_devices:
        if device=='out':
            return 1, 0, 0, 0

        new_paths_none, new_paths_dac, new_paths_fft, new_paths_both = paths_with_dac_fft(device)  

        if device=='dac':
            new_paths_dac += new_paths_none
            new_paths_none = 0
            new_paths_both += new_paths_fft
            new_paths_fft = 0
     
        elif device=='fft':
            new_paths_fft += new_paths_none
            new_paths_none = 0
            new_paths_both += new_paths_dac
            new_paths_dac = 0

        num_paths_none += new_paths_none
        num_paths_dac += new_paths_dac
        num_paths_fft += new_paths_fft
        num_paths_both += new_paths_both
    
    return num_paths_none, num_paths_dac, num_paths_fft, num_paths_both

start_time = timer()

DAY_NUMBER = 11
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

devices = {}
for line in open(FILE_NAME, 'r'):
    tmp_devices = line.strip().split()
    devices[tmp_devices[0][0:-1]] =  tmp_devices[1:]

total_paths_p1 = paths_to_out('you')
total_paths_p2, a,b,c = paths_with_dac_fft('svr')

end_time = timer()

print(total_paths_p1)
print(total_paths_p2)
print(f'Time elapsed: {(end_time - start_time)*1000:.3f} ms')
