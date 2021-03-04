#Q. 33:

#Count High and Low(Strings)

#Write a Python to check whether the given string is palindrome or not
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output


string = input()
if string == string[::-1]:
  print("The string is a palindrome")
else:
  print("The string is not a palindrome")