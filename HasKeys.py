#Q. 75:

#Has Keys(Dictionary)

#Write a program to check whether the given key is present in the dictionary.
#If the key is present then display the value of the entered key and if the key is not present then display the appropriate message
#Input:
#1.Get size of the dictionary
#2. Get the key-value elements
#3. Get the key to be searched
#Output:
#1. Display the dictionary
#2. Print either True or False
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output


s = int(input())
L1 = []
L2 = []
for i in range(s):
  L1.append(int(input()))
for i in range(s):
  L2.append(int(input()))
D = dict(zip(L1,L2))
key = int(input())
print("The dictionary is")
print(D)
if key in D:
  print("True")
else:
  print("False")