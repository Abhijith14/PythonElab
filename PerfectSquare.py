#Q. 57:

#Perfect Square(Lists and Tuples)

#Write a program to display the perfect square using list
#Input:
#1. The lower range number
#2. The upper range number
#Output:
#The perfect square number using List
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output.


import math

l = int(input())
u = int(input())
lst = list()
for i in range(l,u+1):
  root = math.sqrt(i)
  if int(root + 0.5)**2 == i:
    lst.append(i)
print(lst)