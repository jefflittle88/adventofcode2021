
depth_list = []

with open(r'T:\input.txt') as input_file:
    for line in input_file:
        depth = line.rstrip()
        depth_list.append(int(depth))
    input_file.close()

depth_count = 0
increase_count = 0
max_id = len(depth_list)
for reading in depth_list:
    previous_reading_ids = [(depth_count - 1), (depth_count), (depth_count + 1)]
    reading_ids = [(depth_count), (depth_count + 1), (depth_count + 2)]
    if  depth_count > 0 and depth_count < (max_id-2):
        previous_sum = 0
        current_sum = 0
        for id in previous_reading_ids:
            previous_sum += depth_list[id]
        for id in reading_ids:
            current_sum += depth_list[id]
        difference = current_sum - previous_sum
        print(f"The previous sum was {previous_sum} and the current sum is {current_sum}")
        
        if (difference) > 0:
            print (f"Depth increased by {difference}")
            increase_count += 1
        else:
            print("Depth didn't increase")
    
    depth_count += 1

print (f"The depth increased {increase_count} times out of a total possible {max_id} times")
    



