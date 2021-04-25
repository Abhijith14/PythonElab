#Q. 84:

#Finding the multiple(Searching and Sorting)

#Find the multiple of given number in the list of integers
#Input:
#First Line of the Input is the Number of Elements in the List
#Second Line of Input has the elements of the List
#Third line has has the number for which you have to find the multiples
#Output:
#Print the Multiples


s = int(input())
L = []
for i in range(s):
  L.append(int(input()))
key = int(input())
for i in L:
  if i % key == 0:
    print(i)