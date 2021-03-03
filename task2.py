#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(number):
    # input:
    #       a list of number
    #return value: the largest number in the list
    number.sort()
    return   number[-1]
#this should be return a value of 13
x = ([3,1,4,7,13,9])

#this should be return a value of 12.3
y = ([5,1,12.3]) 
