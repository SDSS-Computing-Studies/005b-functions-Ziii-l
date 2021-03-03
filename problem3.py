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
def factor(num,count):
    num=12
    factors=[]
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    print ("Factors of {} = {}".format(num,factors))
    count =37
    factors=[]
    for i in range(1,count+1):
        if count%i==0:
            factors.append(i)
    print ("Factors of {} = {}".format(count,factors))
