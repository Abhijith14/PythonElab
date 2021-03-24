#Q. 53:

#Tom and Jerry(Lists and Tuples)

#Write a program to display the odd and even numbers using a separate list.
#Odd numbers should be in one list and even numbers should be in another list
#Input:
#1. The First input corresponds to number of input elements followed by the list elements
#Output:
#1. Even Numbers in a list
#2. Odd Numbers in a list
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output.


s = int(input())
lst = list()
odd = list()
even = list()
for i in range(s):
  lst.append(int(input()))
for i in range(s):
  if lst[i] % 2 == 0:
    even.append(lst[i])
  else:
    odd.append(lst[i])
print(even)
print(odd)