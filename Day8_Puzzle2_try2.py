import itertools
import time

seven_segment_assignments = {1:'', 2:'', 3:'', 4:'',5:'', 6:'', 7:''}
number_arrangments = {0:[1, 2, 4, 5, 6, 7],1:[2, 4], 2:[1, 2, 3, 5, 6],3:[1, 2, 3, 4, 5],4:[2, 3, 4, 7],5:[1, 3, 4, 5, 7],6:[1, 3, 4, 5, 6, 7],7:[1, 2, 4],8:[1, 2, 3, 4, 5, 6, 7], 9:[1, 2, 3, 4, 5, 7]}
#total_count = 0

# for k,v in digit_list.items():
#     print (f"Key = {k} Value = {v}")


with open(r'C:\input8_sub.txt') as input_file:
    
    for line in input_file:
        
        digit_list = []
        #print(line)
        line_list = line.rstrip().split('|')
        input_value_list = line_list[0].rstrip().split(' ')
        print(input_value_list)
        sorted_input_list = list(sorted(input_value_list, key = len))
        print(sorted_input_list)
        output_value_list = line_list[1].lstrip().split(' ')
        #print(output_value_list)
        time.sleep(30)

        #BRUTE FORCE IT
        i = 0
        #starting_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
        permutations_list = list(itertools.permutations(['a','b','c','d','e','f','g']))
        
        
        for permutation in permutations_list:
            #print(permutation)
            decoded_values_list = []
            for input in sorted_input_list:
                #print(sorted_input_list)
                print(input)
                decoded_value = []
                for letter in input:
                    decoded_value.append(permutation.index(letter)+1)
                decoded_values_list.append(decoded_value)
            #print(decoded_values_list)
        

            for decode in decoded_values_list:
                sorted_loc_list = list(sorted(decode))
                if sorted_loc_list in number_arrangments.values():
                        #print(sorted_loc_list)
                        #print(seven_segment_assignments)
                        #print("yay?")
                        i += 1
                else:
                    continue
                    #print("Boo!")

                if i < 7:
                    print(f"i = {i}")
                    continue
                    time.sleep(2)

                if i == 7:
                    print("Seven Matches?")
                    print(f"i = {i}")
                    print(permutation)
                    for letter in permutation:
                        for k,v in seven_segment_assignments.items(): 
                            if (permutation.index(letter) + 1) == k:
                                seven_segment_assignments[k] = letter 
                                        
                    break
                
        print(seven_segment_assignments)
        time.sleep(30)
        # final_answer = []
        # for item in output_value_list:
        #     print(item)
        #     answer_list = []
        #     output_list =  [char for char in item]
        #     for output in output_list:
        #             for k,v in seven_segment_assignments.items():
        #                 if output == v:
        #                     answer_list.append(k)
        #     sorted_answer_list = list(sorted(answer_list))
        #     print(sorted_answer_list)
        #     # for sorted_answer in sorted_answer_list:
        #     #     print(sorted_answer)
        #     for k,v in number_arrangments.items():
        #         if sorted_answer_list == v:
        #             print(k)
        #             final_answer.append(k)
        #         else:
        #             print("no match")
        #             continue

        # print(final_answer)
            



        
""" 

        #     if len(input) == 2:
        #         input_list =  [char for char in input]
        #         seven_segment_assignments[2] = input_list[0]
        #         seven_segment_assignments[4] = input_list[1]
        #     elif len(input) == 3:
        #         input_list =  [char for char in input]
        #         already_assigned = f"{seven_segment_assignments[2]}{seven_segment_assignments[4]}"
        #         for record in input_list:
        #             if record in already_assigned:
        #                 continue
        #             else:
        #                 seven_segment_assignments[1] = record
        #     elif len(input) == 4:
        #         input_list =  [char for char in input]
        #         already_assigned = f"{seven_segment_assignments[2]}{seven_segment_assignments[4]}"
        #         for record in input_list:
        #             #print (record)
        #             if record in already_assigned:
        #                 continue
        #             elif seven_segment_assignments[3] == '':
        #                 seven_segment_assignments[3] = record
        #             else:
        #                 seven_segment_assignments[7] = record

               
        #     elif len(input) == 5:
        #         print("Input is 5 characters long")
        #         input_list =  [char for char in input]
        #         #already_assigned = f"{seven_segment_assignments[2]}{seven_segment_assignments[4]}{seven_segment_assignments[1]}{seven_segment_assignments[3]}"
        #         already_assigned = f"{seven_segment_assignments[2]}{seven_segment_assignments[4]}{seven_segment_assignments[1]}{seven_segment_assignments[3]}{seven_segment_assignments[7]}"
        #         for record in input_list:
        #             print(record)
        #             # if record in already_assigned:
        #             #     continue
        #             # if len(record) == 1:
        #             #     seven_segment_assignments[5] = record
        #             # elif len(record) == 2:
        #             #     print("THE RECORD LENGTH IS 2??!?!?!?!?!?!?!?!?!?!?!!?!?!?!?!?!?!?!?!?!")
        #             #     if seven_segment_assignments[5] == '':
        #             #         seven_segment_assignments[5] = record
        #             #     else: 
        #             #         seven_segment_assignments[6] = record
        #             if record in already_assigned:
        #                 continue  
        #             if seven_segment_assignments[5] == '':
        #                 seven_segment_assignments[5] = record
        #             elif seven_segment_assignments[6] == '':
        #                 seven_segment_assignments[6] = record
        #             else:
        #                 continue

                    

        #     else:
        #         input_list =  [char for char in input]
        #         already_assigned = f"{seven_segment_assignments[2]}{seven_segment_assignments[4]}{seven_segment_assignments[1]}{seven_segment_assignments[5]}{seven_segment_assignments[7]}{seven_segment_assignments[3]}"
        #         for record in input_list:
        #             if record in already_assigned:
        #                 continue
        #             else:
        #                 seven_segment_assignments[6] = record
        # fivers = []            
        # for input in sorted_input_list:
            
        #     if len(input) == 5:
        #         fivers.append(input)
        
        # print(fivers)
        # three_seven_swap = False
        # five_six_swap = False
        # repeat_flag = True
        # i = 0
        # while i < 3:
        #     for fiver in fivers:
        #         loc_list = []
                
        #         input_list =  [char for char in fiver]
        #         print(input_list)
        #         for record in input_list:
        #             for k,v in seven_segment_assignments.items():
        #                 if record == v:
        #                     loc_list.append(k)
        #         sorted_loc_list = list(sorted(loc_list))

        #         print(loc_list)
        #         print(sorted_loc_list)
                
        #         print(number_arrangments.values())


            if sorted_loc_list in number_arrangments.values():
                #print(seven_segment_assignments)
                print("yay?")
            
            else:
                print("nay...?")
                if three_seven_swap == False:
                    three =  seven_segment_assignments[3]
                    seven = seven_segment_assignments[7]
                    seven_segment_assignments[3] = seven
                    seven_segment_assignments[7] = three
                    three_seven_swap = True
                    break
                elif five_six_swap == False:
                    # Undo our original changes
                    three =  seven_segment_assignments[3]
                    seven = seven_segment_assignments[7]
                    seven_segment_assignments[3] = seven
                    seven_segment_assignments[7] = three
                    # Make new changes...yay?
                    five =  seven_segment_assignments[5]
                    seven = seven_segment_assignments[7]
                    seven_segment_assignments[6] = seven
                    seven_segment_assignments[7] = five
                    five_six_swap = True
                    break
                else:
                    break
        #i += 1            
                #print(seven_segment_assignments)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(sorted_input_list)
        for input in sorted_input_list:
            print(input)
            
            loc_list = []
                
            input_list =  [char for char in input]
            print(input_list)
            for record in input_list:
                for k,v in seven_segment_assignments.items():
                    if record == v:
                        loc_list.append(k)
            sorted_loc_list = list(sorted(loc_list))
            print(sorted_loc_list)
            
            if sorted_loc_list in number_arrangments.values():
                    #print(seven_segment_assignments)
                    print("yay?")
                
            else:
                print("nay...?")
                    



        print(seven_segment_assignments)
        final_answer = []
        for digit in output_value_list:
            print(digit)
            answer_list = []
            output_list =  [char for char in digit]
            
            for output in output_list:
                for k,v in seven_segment_assignments.items():
                    if output == v:
                        answer_list.append(k)
            sorted_answer_list = list(sorted(answer_list))
            # for sorted_answer in sorted_answer_list:
            #     print(sorted_answer)
            for k,v in number_arrangments.items():
                if sorted_answer_list == v:
                    print(k)
                    final_answer.append(k)
                else:
                    #print("no match")
                    continue
        print(final_answer)
        # for number in final_answer:
        #     print(number)


        #print(sorted_answer_list)
        


            

            
                        

        # for digit in output_value_list:
        #     if len(digit) == 2:
        #         print(digit)
        #         digit_list.append(1)
        #         #total_count += 1
        #     elif len(digit) == 4:               
        #         digit_list.append(4)
        #         #total_count += 1
        #     elif len(digit) == 3:
        #         digit_list.append(7)
        #         #total_count += 1
        #     elif len(digit) == 7:
        #         digit_list.append(8)
        #         #total_count += 1
        #     else:
        #         digit_list.append(99)
                
        #print(digit_list)

#print(digit_list)
#print(total_count)
 """
input_file.close()

