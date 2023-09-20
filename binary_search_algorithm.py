# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:26:57 2023

@author: nicola

Implement the binary search algorithm in Python – i.e. the recursive function def
binary_search(item, ordered_list, start, end). It takes an item to
search (i.e. item), an ordered list and a starting and ending positions in the list as input.
It returns the position of item in the list if it is in it and None otherwise. The binary
search first checks if the middle item of the list between start and end (included) is
equal to item, and returns its position in this case. Otherwise, if the central item is less
than item, the algorithm continues the search in the part of the list that follows the
middle item. Instead, if the central item is greater than item, the algorithm continues the
search in the part of the list preceeding the central item. Accompany the implementation
of the function with the appropriate test cases.

"""

##CAUTION: this works only for ORDERED_LISTS!!

x = ["Brian", "Joe", "Lois", "Meg", "Peter", "Stewie"]

def binary_search(item, ordered_list):
    start = 0
    end = len(ordered_list) -1
    try:
        x.index(item)
    except ValueError:
        print("'item' is not in the list")
    while start <= end: #this goes on if in the list there is no signle number
        mid = (start + end)//2
        midpoint = ordered_list[mid]#this convertes the mid as a number to the midpoint as a str
                                    #so that we can work with str comparison                                                
        if midpoint == item:
            return mid
        elif midpoint < item:
            start = mid 
        else:
            end = mid
       
              

def test_binary_search(item, ordered_list, expected):
    result = binary_search(item, ordered_list)
    if result == expected :
        return True 
    else:
        return False


print(test_binary_search('Peter', x, 4))
print(test_binary_search('Peter', x, 3))
print(test_binary_search('peter', x, 4))


