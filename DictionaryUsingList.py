#Q. 71:

#Dictionary Using List(Dictionary)

#Write a program to get the input of key and value of the element in dictionary.
#Display the key-value pair in the python dictionary format.
#Kindle get the input using List Concept.
#Input:
#1. Size of first list
#2. Elements of first list
#3. Size of second list
#4. Elements of second list
#Output:
#1. The first list elements are keys of the dictionaries
#2. The second list elements are corresponding elements of the dictionaries


s1 = int(input())
L1 = []
L2 = []
for i in range(s1):
  L1.append(int(input()))
s2 = int(input())
for i in range(s2):
  L2.append(int(input()))

D = dict(zip(L1,L2))
print(D)