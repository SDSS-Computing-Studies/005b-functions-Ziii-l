#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10

output 
[1,2,5,10]
(2 points)
"""
def factor(num):
    #input: parameter is a positive integer
    #output: a sorted list of all the factor of that number
    list=[]
    for i in range( 1,num+1):
        if num % i==0:
            list.append(i)
            print ("Factors of {} = {}".format(num,list))    

parameter1 = 12
parameter2 = 37


