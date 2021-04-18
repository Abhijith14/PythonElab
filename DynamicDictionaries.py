#Q. 77:

#Dynamic Dictionaries(Dictionary)

#Write a program to print all the squares of the range from 1 to n
#Input:
#1.Get the Value
#Output:
#1. Display the square value of the dictionary
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output


k = int(input())
D = {}
for i in range(1,k+1):
  D[i] = i**2
print(D)