import random
import os
mystr = ("_   "*5)
len_ofstr = (len(mystr))
word = "apple"
#print(mystr)
#print(len_ofstr)

while True:
    print(mystr)
    #print(len_ofstr)
    player_input = input("> ")
    input_to_list = []
    
    for i in player_input:
        input_to_list.append(i)
    
   # print(input_to_list)
    
    for i in input_to_list:
        index = 0
        if i == word[index]:
            print("Found a match")
            index += 1

            