from timeit import default_timer as timer

start_time_1 = timer()

DAY_NUMBER = 6
TEST = False

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    data_stream = file.read().strip()

for i in range(3,len(data_stream)):
    most_recent_chars = data_stream[i-3:i+1]
    if len(set(most_recent_chars))==4:
        num_characters_packets = i+1
        break

for i in range(13,len(data_stream)):
    most_recent_chars = data_stream[i-13:i+1]
    if len(set(most_recent_chars))==14:
        num_characters_messages = i+1
        break

end_time_1 = timer()

print(num_characters_packets)
print(num_characters_messages)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
