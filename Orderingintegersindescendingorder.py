#Q. 89:

#Ordering integers in descending order(Searching and Sorting)

#Sort the given set of integers using bubble sort and print from largest to smallest integer


s = int(input())
L = []
ans = []
for i in range(s):
  L.append(int(input()))
L.sort()
s = s - 1
while s >= 0:
  ans.append(L[s])
  s = s - 1
print(ans)