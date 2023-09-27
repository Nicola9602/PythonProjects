
'''
Implement the divide and conquer quicksort algorithm in Python – i.e. the recursive def
quicksort(input_list, start, end) . First, it takes a list and the positions of
the first and last elements to consider as inputs. Then, it calls
partition(input_list, start, end, start) (defined in the previous
exercise) to partition the input list into two slices. Finally, it executes itself recursively on
the two partitions (neither includes the pivot value since it has already been correctly
positioned through the partition execution). In addition, define the base case of the
algorithm appropriately to stop if needed before running the partition algorithm.
Accompany the implementation of the function with the appropriate test cases.

'''

my_list = list(["The Graveyard Book",
"Coraline", "Neverwhere", "Good Omens", "American Gods"])

from partition_algorithm import partition

def quicksort(input_list, start, end):
    if start < end :
        pivot_position = partition(input_list, start, end, start)
        quicksort(input_list, start, pivot_position -1)
        quicksort(input_list, pivot_position + 1, end) 
        
    return input_list
       


def test_quicksort(input_list, start, end, expected):
    result = quicksort(input_list, start, end)
    if expected == result:
        return True
    else:
        return False
    
    
    
print(test_quicksort([1], 0, 0, [1]))
print(test_quicksort([1, 2, 3, 4, 5, 6, 7], 0, 6, [1, 2, 3, 4, 5, 6, 7]))
print(test_quicksort([3, 4, 1, 2, 9, 8, 2], 0, 6, [1, 2, 2, 3, 4, 8, 9]))
print(test_quicksort(["Coraline", "American Gods", "The Graveyard Book", "Good Omens", "Neverwhere"], 0, 4,
                     ["American Gods", "Coraline", "Good Omens", "Neverwhere", "The Graveyard Book"]))
