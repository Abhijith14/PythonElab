#Q. 58:

#Club Me - Club two lists(Lists and Tuples)

#Write a program to merge two list using functions
#Input:
#1. The First input corresponds to number of input elements followed by the list elements
#2. The Second input the size of second list followed by its elements
#Output:
#Sorted List
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output.


def sortlst(lst):
  lst.sort()
  return lst

l1 = list()
l2 = list()
s1 = int(input())
for i in range(s1):
  l1.append(int(input()))
s2 = int(input())
for i in range(s2):
  l2.append(int(input()))
print("Sorted list is:",sortlst(l1+l2))