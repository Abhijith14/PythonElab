#Q. 74:

#Multiple(Dictionary)

#Write a program to add multiply dictionaries
#Input:
#1.Get two dictionaries key-value elements
#Output:
#1. Display the first dictionary
#2. Display the second dictionary
#3. Display the concatenated dictionary
#4. Display the total product of the values in the dictionaries
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output


s = 1
k1 = int(input())
D1 = {}
D1[k1] = int(input())
k2 = int(input())
D2 = {}
D2[k2] = int(input())
print("First Dictionary")
print(D1)
print("Second Dictionary")
print(D2)
print("Concatenated dictionary is")
D1.update(D2)
print(D1)
print("Total sum of values in the dictionary")
for i in D1.values():
  s = s * i
print(s)