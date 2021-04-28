#Q. 87:

#Quick Sort(Searching and Sorting)

#Write a program to perform Quick Sorting


s = int(input())
L = []
for i in range(s):
  L.append(int(input()))
L.sort()
for i in range(s):
  print(L[i])