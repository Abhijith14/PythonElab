#Q. 32:

#Count it(Strings)

#Write a Python program to count the number of entered words in a given string
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output
#Input:
#1. First Line: String or sentence
#2. Second Line: word to be searched in the sentence
#Output:
#Word Count


string = input()
word = input()
c = 0
lst = list(string.split(" "))
for i in range(len(lst)):
  if word == lst[i]:
    c = c + 1
print(c)