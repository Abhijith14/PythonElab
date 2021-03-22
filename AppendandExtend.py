#Q. 51:

#Append and Extend(Lists and Tuples)

#Write a program to append two list and display the extended or appended list
#Input:
#1. The Size of First List
#2. The Size of Second List
#3. First List elements
#4. Second List elements
#Output:
#Appended Single List
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output.


s1 = int(input())
s2 = int(input())
l1 = list()
l2 = list()
for i in range(s1):
  l1.append(int(input()))
for i in range(s2):
  l2.append(int(input()))
print(l1+l2)