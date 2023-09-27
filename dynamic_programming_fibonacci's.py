# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:54:52 2023

Use dynamics programming to calculate the nth fibonacci's number. 
Insstead of calculating it ex novo each time, which is expensive 
in terms of algorithmic power, it checks if the number is already in a dictionary. 


@author: nicol

"""


def test_fib_dp(n,d,expected):
    result = fib_dp(n, d)
    if result == expected :
        return True
    else:
        return False
 

def fib_dp(n,d): 
    if n not in d:  # Checking if a solution exists
        if n <= 0:
            return 0
        elif n == 1:
            return 1 
        else: # recursive step
# the dictionary will be passed as input of the recursive
# calls of the function
            d[n] = fib_dp(n-1, d) + fib_dp(n-2, d) #this inserts a new number in position n
                                                   #in the dictionary, 
                                                   # following the fibonacci's rule
    
    return d.get(n)


print(test_fib_dp(0, dict(), 0))
print(test_fib_dp(1, dict(), 1))
print(test_fib_dp(2, dict(), 1))
print(test_fib_dp(7, dict(), 13)) 