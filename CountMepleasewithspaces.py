#Q. 36:

#Count Me please with spaces(Strings)

#Write a Python program to count the number of lower-case letter, uppercase letters and spaces in the entered string.
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output
#Output:
#First Line: Lowercase count
#Second Line: Uppercase count
#Third Line: Spaces count in the string


string = input()
l = u = s = 0
for i in range(len(string)):
  if string[i] == " ":
    s = s + 1
  elif str.isupper(string[i]):
    u = u + 1
  elif str.islower(string[i]):
    l = l + 1
print(l)
print(u)
print(s)