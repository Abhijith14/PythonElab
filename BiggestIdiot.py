#Q. 40:

#Biggest Idiot(Strings)

#Write a Python program to find the biggest string based on the length function.
#The user should get two string inputs and compare the string
#Print the longest or biggest string in the output.
#If the strings are equal then print the message as "Both strings are equal"
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output.


string1 = input()
l1 = len(string1)
string2 = input()
l2 = len(string2)
if l1 > l2:
  print("Larger string is:")
  print(string1)
elif l2 > l1:
  print("Larger string is:")
  print(string2)
else:
  print("Both strings are equal")
