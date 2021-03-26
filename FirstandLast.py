#Q. 55:

#First and Last(Lists and Tuples)

#Write a program to interchange or swap the first and last number in the list
#Input:
#1. The size of the list
#2. List Elements
#Output:
#The new list with first and last numbers exchanged
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output.


s = int(input())
lst = list()
for i in range(s):
  lst.append(int(input()))
temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp
print("New list is:")
print(lst)