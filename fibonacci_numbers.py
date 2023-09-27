# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:55:50 2023
this code defines a function that behaves like fibonacci's sequence
basicalli it takes anumber as an input, which is the e.g., 30th fibonacci's
sequence number, and it returns that number. 
For example, the third fibonacci's sequence number is 2, 
so if you input fib(3) you get 2 as an answer. 
the 30th fibonacci's sequence number instead is 832040

the test fib is a function that tests whether the function fib is working 
properly and does so through the four print statements below

@author: nicol
"""

def test_fib(n, expected):
    result = fib(n)
    if result == expected:
        return True
    else:
        return False
    

def fib(n):
    if n <= 0 :
        return 0
    elif n == 1:
        return 1
    else: 
        return fib(n-1) + fib(n -2)
        
        
        
print(test_fib(0, 0))
print(test_fib(1, 1))
print(test_fib(2, 1))
print(test_fib(7, 13))

