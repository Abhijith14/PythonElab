#Q. 59:

#Longest word(Lists and Tuples)

#Python Program to Read a List of Words and Return the Length of the Longest One
#Input:
#First Line has the Number of Words the followed by the words
#Output:
#Print the longest word in the list.


s = int(input())
lst = list()
max = 0
for i in range(s):
  lst.append(input())
for i in range(s):
  if len(lst[i]) > max:
    max = len(lst[i])
    string = lst[i]
print(string)