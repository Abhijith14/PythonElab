#Q. 90:

#Searching Linear(Searching and Sorting)

#Write a program to search a element linearly


s = int(input())
L = []
for i in range(s):
  L.append(int(input()))
key = int(input())
for i in range(s):
  if L[i] == key:
    print("Element is present at index",i)