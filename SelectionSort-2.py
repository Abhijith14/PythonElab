#Q. 82:

#Selection Sort - 2(Searching and Sorting)

#Sort the given set of numbers using Selection Sort. The first line of the input contains the number of elements, the second line of the input contains the numbers to be sorted. In the output print the status of the array at the 4th iteration and the final sorted array in the given format


import sys 

s = int(input())
A = []
for i in range(s):
  A.append(int(input()))

for i in range(s): 
    min_idx = i 
    for j in range(i+1, s): 
        if A[min_idx] > A[j]: 
            min_idx = j 
    A[i], A[min_idx] = A[min_idx], A[i]
    if i == 2:
      for i in range(s):
        if i == s-1:
          print(A[i])
        else:
          print(A[i],end = " ")
print ("Sorted Array") 
for i in range(s): 
  if i == s-1:
    print(A[i])
  else:
    print(A[i],end = " ") 