# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:44:41 2023

@author: nicola


Write in Python the function def my_range(stop_number), which behave like the
built-in function range() introduced in Section "Insertion sort" and returns a proper list,
and accompany the function with the related test case. It is not possible to use the
built-in function range() in the implementation.

"""
#defining the funciton my_range 

def my_range(stop_number):
    output_list = [];#creates an empty list in the variable  
    if stop_number > 0: #range(0) gives an empty list
        output_list.append(stop_number - stop_number); #this creates the first element, that is 0
        for n in output_list:
            if n != stop_number -1: #tells it up to which number to keep appening it
                output_list.append(output_list[n] +1);
        return output_list;      
    else:
        return[]#returns an empty list if stop_number is less or equal to 0

def test_my_range(stop_number, expected):
    result = my_range(stop_number)
    if result == expected :
        return True
    else:
        return False
    

print(test_my_range(4, [0,1,2,3]))
print(test_my_range(0, []))
print(test_my_range(-1, []))
print(test_my_range(4, [0,1,2,]))

