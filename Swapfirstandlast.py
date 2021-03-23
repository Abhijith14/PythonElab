#Q. 52:

#Swap first and last(Lists and Tuples)

#Python Program to Swap the First and Last Value of a List
#Input:
#First Line:Number of elements in list 
#Second Line:Elements of the List
#Output:
#Print the new list after swapping


s = int(input())
lst = list()
for i in range(s):
  lst.append(int(input()))
temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp
print("New list is:")
print(lst)