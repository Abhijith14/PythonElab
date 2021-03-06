#Q. 35:

#Words and Characters(Strings)

#Write a Python program to count the number of words and characters in a given string
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output.


string = input()
lst1 = list(string.split(" "))
lst2 = list(string)
print(len(lst1))
print(len(lst2))