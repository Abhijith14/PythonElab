#Q. 42:

#Sine series(Functions)

#Python Program to Find the Sum of Sine Series
#Input
#First Line : The value of x in degrees
#Second Line: The number of terms
#Output
#Print the Sum of Sine series


import math
def sin(x,n):
    s = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        s = s + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return s
x=int(input())
n=int(input())
print(round(sin(x,n),2))