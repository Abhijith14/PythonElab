#Q. 85:

#Find Mid-term With ODD and Even length of list(Searching and Sorting)

#Perform sorting on list of integers and print the mid-term.


s = int(input())
L = list()
for i in range(s):
  L.append(int(input()))
L.sort()
print("Sorted List:")
print(L)
print("Mid-term:")
n = int(s/2)
if s % 2 == 0:
  print(L[n-1])
else:
  print(L[n])