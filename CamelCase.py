#Q. 34:

#CamelCase(Strings)

#Alice wrote a sequence of words in CamelCase as a string of letters, S, having the following properties:
#1. It is a concatenation of one or more words consisting of English letters.
#2. All letters in the first word are lowercase.
#3. For each of the subsequent words, the first letter is uppercase and rest of the letters is lowercase.
#Given S, print the number of words in S on a new line.
#Input:
#A single line containing string S.
#Output:
#Print the number of words in string S.


string = input()
c = 0
for i in range(len(string)):
  if str.isupper(string[i]):
    c = c + 1
print(c+1)