#Q. 81:

#Finding the occurrence of an integer(Searching and Sorting)

#Find the given integer in the given list of integers  and print the number of occurrences of that integer in the list.


s = int(input())
L = []
for i in range(s):
  L.append(int(input()))
key = int(input())
print(L.count(key))