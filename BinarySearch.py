#Q. 83:

#Binary Search(Searching and Sorting)

#Write a program to implement binary search algorithm


def binarySearch (arr, l, r, x): 
  
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        return -1
  
L = int(input())
arr = []
for i in range(L):
  arr.append(int(input()))
S = int(input())
ele = []
for i in range(S):
  ele.append(int(input()))
result = []
for i in range(S):
  result.append(binarySearch(arr, 0, len(arr)-1, ele[i]))
f = 0
for i in range(S):
  if result[i] == -1: 
    f = 0
    break
  else: 
    f = 1
if f == 0:
  print("Not found")
else:
  print("Sequence found between index " + str(result[0]) + " and " + str(result[-1]+1))