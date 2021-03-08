#Q. 37:

#Who is least here(Strings)

#Write a Python program to count the number of lower-case letters in the entered string.
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output.


string = input()
c = 0
for i in range(len(string)):
  if str.islower(string[i]):
    c = c + 1
print(c)