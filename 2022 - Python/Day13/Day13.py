from timeit import default_timer as timer

def string_to_list(input_string):
    output_list = []

    tmp_string = input_string[1:-1]

    sub_items = tmp_string.split(',')

    for sub_item in sub_items:
        if sub_item[0]=='[':
            close_idx = sub_item.find(']')
            output_list.append(string_to_list(sub_item[0:close_idx+1]))
        else:
            output_list.append(int(sub_item))

    return output_list

def compare_packets(packet_1, packet_2):
    for value_1, value_2 in zip(packet_1, packet_2):
        if isinstance(value_1, int) and isinstance(value_2, int):
            if value_2 < value_1:
                return 0
        
        elif isinstance(value_1, list) and isinstance(value_2, list):
            return compare_packets(value_1, value_2)
        
        else:
            if isinstance(value_1, int):
                value_1 = [value_1]
            else:
                value_2 = [value_2]
            
            return compare_packets(value_1, value_2)

start_time_1 = timer()

DAY_NUMBER = 13
TEST = True

if TEST:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Example.txt"
else:
    FILE_NAME = "Day" + str(DAY_NUMBER) + "/Input.txt"

with open(FILE_NAME, 'r') as file:
    packets = [line.strip() for line in file]

num_pairs = (len(packets) + 1)//3
index_sum = 0

for i in range(num_pairs):
    packet_1 = packets[3*i]
    packet_2 = packets[3*i+1]

    list_1 = string_to_list(packet_1)
    list_2 = string_to_list(packet_2)


    # if compare_packets(packet_1, packet_2):
    #     index_sum += i

end_time_1 = timer()

print(index_sum)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')
