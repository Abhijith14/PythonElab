#Q. 80:

#Display Values(Dictionary)

#Write a program to display only the values of the keys in the output
#Input:
#1.Get two dictionaries key-value elements
#Output:
#1. Display the first dictionary
#2. Display the second dictionary
#3. Display the concatenated dictionary
#4. Display the values of the concatenated dictionary
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output


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
print("The Values of Dictionary")
print(list(D1.values()))