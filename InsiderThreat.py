#Q. 31:

#Insider Threat(Strings)

#Write a Python program to find the substring in the given string
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output
#Input:
#1. Sentence
#2. The word to be searched
#Output:
#Case 1: If the string is present then print "Substring in string"
#Case 2: If the string is not present then print "Substring not found in string"


string = input()
word = input()
lst = list(string.split(" "))
for i in range(len(lst)):
  if word == lst[i]:
    f = 1
    break
  else:
    f = 0;
if f == 1:
  print("Substring in string")
else:
  print("Substring not found in string")
               