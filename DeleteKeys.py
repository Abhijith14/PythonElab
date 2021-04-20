#Q. 79:

#Delete Keys(Dictionary)

#Write a program to delete the keys in the dictionaries
#Input:
#1.Get Four dictionaries key-value elements
#2. The Key to be deleted
#Output:
#1. Display the first dictionary
#2. Display the second dictionary
#3. Display the third dictionary
#4. Display the fourth dictionary
#5. Display the concatenated dictionary
#6. Display the updated dictionaries
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output


k1 = int(input())
D1 = {}
D1[k1] = int(input())
k2 = int(input())
D2 = {}
D2[k2] = int(input())
k3 = int(input())
D3 = {}
D3[k3] = int(input())
k4 = int(input())
D4 = {}
D4[k4] = int(input())
KEY = int(input())
print("First Dictionary")
print(D1)
print("Second Dictionary")
print(D2)
print("Third Dictionary")
print(D3)
print("Fourth Dictionary")
print(D4)
print("Concatenated dictionary is")
D1.update(D2)
D1.update(D3)
D1.update(D4)
print(D1)
n = D1.pop(KEY,"Key not found")
if n != "Key not found":
  print("Updated dictionary")
  print(D1)
else:
  print(n)