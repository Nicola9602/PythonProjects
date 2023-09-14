# -*- coding: utf-8 -*-
"""
from collections import deque

#algorithms thatb takes a list as an input and creates a stack 
#with all the list's values as an outputs
def stack_from_list(input_list):
    output_stack = deque() #the stack to create
    #iterarte each element in the input list and add it to the stack 
    for item in input_list:
        output_stack.append(item);
    return output_stack
        
def test_stack_from_list(input_list, expected):
    result = stack_from_list(input_list)
    if result == expected :
        return True
    else:
        return False 
    
print(test_stack_from_list([1, 2, 3], deque(1, 2, 3)))
print(test_stack_from_list([1, 2, 3], [12, 32, 31]))

Write in Python the function def my_enumerate(input_list), which behaves like
the built-in function enumerate() introduced in Section "Linear search" and returns a
proper list, and accompany the function with the related test case. It is not possible to
use the built-in function enumerate() in the implementation.

"""
input_list = ["Coraline", "American Gods",
"The Graveyard Book", "Good Omens",
"Neverwhere"]

def my_enumerate(input_list):
    output_list = [] #creates a empty list 
    for item in input_list : #loops through the existin list
        position = input_list.index(item); #stores the index of the item in the variable position
        output_list.append((position, item))
    print(output_list);
    
def test_my_enumerate(input_list, expected):
    result = my_enumerate(input_list)
    if result == expected :
        return True
    else:
        return False 

#test run

print(test_my_enumerate(input_list, [(0, 'Coraline'), (1, 'American Gods'), (2, 'The Graveyard Book'), (3, 'Good Omens'), (4, 'Neverwhere')]))
print(test_my_enumerate(input_list, [(1, 'American Gods'), (2, 'The Graveyard Book'), (3, 'Good Omens'), (4, 'Neverwhere')]))