# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 11:59:10 2023

@author: nicola

Write in Python the function def my_reversed(input_list), which behave like the
built-in function reversed() introduced in Section "Insertion sort" and returns a proper
list, and accompany the function with the related test case. It is not possible to use the
built-in function reversed() in the implementation.

The other function is reversed(<input_list>). This function takes a list as input. It returns
a kind of list, i.e. an iterator for iterating the items in the list in reversed order. Thus, for instance,
reversed(list([0, 1, 2, 3])) returns iterator([3, 2, 1, 0]). We can use
these two functions in combination. They allow us to obtain the positions of the items already
ordered in past iterations of the algorithm. For instance, reversed(range(2)) returns
iterator(range([1, 0])) starting from the position (i.e. 2) of the third item in the input
list.

"""

def my_reversed(input_list):
    output_list = [] #creates a new list
    len(input_list) == len(output_list)
    for item in input_list:
        output_list.insert(0, item)
    return output_list

def test_my_reversed(input_list, expected):
    result = my_reversed(input_list);
    if result == expected:
        return True
    else:
        return False

#Tests 
print(test_my_reversed([3, 4, 1, 2, 9, 2], [2, 9, 2, 1, 4, 3]))

print(test_my_reversed([2, 9, 2, 1, 4, 3], [2, 9, 2, 1, 4, 3]))