#Q. 60:

#Biggest Number(Lists and Tuples)

#Write a program to find the biggest of "n" numbers using List
#Input:
#1. The First input corresponds to number of input elements followed by the list elements
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output.


s = int(input())
lst = list()
for i in range(s):
  lst.append(int(input()))
print("Largest element is")
print(max(lst))