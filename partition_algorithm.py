# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:35:55 2023

@author: nicola

Implement in Python the partition algorithm – i.e. the non-recursive function def
partition(input_list, start, end, pivot_position). It takes a list and
the positions of the first and last elements to consider as inputs. It redistributes all the
elements of a list having position included between start and end on the right of the
pivot value input_list[pivot_position] if they are greater than it, and on its left
otherwise – note: pivot_position must be a value between start and end
(included). Also, the algorithm returns the new position where the pivot value is now
stored. For instance, considering my_list = list(["The Graveyard Book",
"Coraline", "Neverwhere", "Good Omens", "American Gods"]), the
execution of partition(my_list, 1, 4, 1) changes my_list as follows:
list(["The Graveyard Book", "American Gods", "Coraline",
"Neverwhere", "Good Omens"]) and 2 will be returned (i.e. the new position of
"Coraline"). Note that "The Graveyard Book" has not changed its position in the
previous execution since it was not included between the specified start and end
positions (i.e. 1 and 4, respectively). Accompany the implementation of the function with
the appropriate test cases. As supporting material, Ang recorded a video that is useful to
understand the rationale of the partition steps.
"""

#my_list = list(["The Graveyard Book",
#"Coraline", "Neverwhere", "Good Omens", "American Gods"])


#I'll start by defining a swap function 

def swap(input_list, old_index, new_index):
    cur_value = input_list[old_index]
    input_list[old_index] = input_list[new_index]
    input_list[new_index] = cur_value


def partition(input_list, start, end, pivot_position):
    pivot = input_list[pivot_position] #this extracts the value of the pivot element from input_list
                                       # base pivot_position in the list 
                                       # e.g input_list[2] = 'Coraline'
    
    swap_index = start - 1   #swap_index is the element the pivot is going to be exchanged with in case
                             #this element is < pivot
    
    for index in range(start, end+1): #this loops through the list, is the task j has in the explanation
        if pivot > input_list[index]:
           swap_index += 1
           swap(input_list, index, swap_index) 
           if swap_index == pivot_position:
              pivot_position = index
           
              
    new_pivot_position = swap_index + 1
    swap(input_list, pivot_position, new_pivot_position)
    
    return new_pivot_position
    
    
def test_partition(input_list, start, end, pivot_position, expected): 
    result = partition(input_list, start, end, pivot_position)
    if result == expected :
        return True
    else:
        return False
    
    
print(test_partition([1, 2, 3, 4, 5], 0, 4, 0, 0))
print(test_partition([4, 5, 3, 1, 7], 0, 4, 0, 2))
print(test_partition([4, 5, 3, 1, 7], 0, 4, 2, 1))
print(test_partition([7, 5, 3, 1, 4], 0, 4, 4, 2))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 1, 8))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 0, 0))
print(test_partition([1, 9, 7, 5, 9, 3, 1, 4, 2, 3], 0, 9, 3, 6))
print(test_partition([1, 2, 2, 3, 9, 8, 4], 1, 2, 1, 1))



