#Q. 73:

#Delete(Dictionary)

#Write a program to delete the key and value of the Dictionary. 
#Define the dictionary in the program as follows 
#The Dictionary is as follows
#dict = {2:4,3:9,4:16,5:25}
#Input:
#1. Get the key that needs to be deleted
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output


dict = {2:4,3:9,4:16,5:25}
k = int(input())
del dict[k]
print(dict)