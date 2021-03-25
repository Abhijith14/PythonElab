#Q. 54:

#Index and Extend(Lists and Tuples)

#Write a program to append two list and find the list index of the list element
#Input:
#1. The Size of First List
#2. The Size of Second List
#3. First List elements
#4. Second List elements
#5. First List Element to be searched
#6. Second List Element to be searched
#Output:
#1. Extended List or appended list
#2. The index of the first list element (entered by user, Step 5)
#3. The index of the second list element (entered by user, Step 6)
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output.


s1 = int(input())
s2 = int(input())
lst1 = list()
lst2 = list()
for i in range(s1):
  lst1.append(int(input()))
for i in range(s2):
  lst2.append(int(input()))
ele1 = int(input())
ele2 = int(input())
lst = lst1+lst2
print("The Extended List")
print(lst)
print("Index for",ele1,"=",lst.index(ele1))
print("Index for",ele2,"=",lst.index(ele2))