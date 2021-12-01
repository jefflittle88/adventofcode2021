
depth_list = []

with open(r'T:\input.txt') as input_file:
    for line in input_file:
        depth = line.rstrip()
        depth_list.append(int(depth))
    input_file.close()

depth_count = 0
increase_count = 0
for reading in depth_list:
    print(reading)
    previous_reading_id = depth_count - 1
    if previous_reading_id >= 0:
        if (reading - depth_list[previous_reading_id]) > 0:
            print (f"Depth increased by {reading - depth_list[previous_reading_id]}")
            increase_count += 1
        else:
            print("Depth didn't increase")
    
    depth_count += 1

print (f"The depth increased {increase_count} times out of a total possible {len(depth_list)} times")
    



