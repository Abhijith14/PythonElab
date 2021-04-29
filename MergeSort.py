#Q. 88:

#Merge Sort(Searching and Sorting)

#Write  a program to perform merge sorting.


s = int(input())
L = []
for i in range(s):
  L.append(int(input()))
L.sort()
for i in range(s):
  print(L[i])