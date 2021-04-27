#Q. 86:

#Find increment sequence(Searching and Sorting)

#Perform sorting on list of integers and print the sequence showing order of increment.


s = int(input())
t = input().split()
L = []
ans = []
for i in range(s):
  L.append(int(t[i]))
L.sort()
print("Sorted List:")
print(L)
for i in range(s-1):
  ans.append(L[i+1]-L[i])
print("Sequence of increments:")
print(ans)