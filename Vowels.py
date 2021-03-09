#Q. 38:

#Vowels(Strings)

#Implement the following algorithm     
#                              
#1. Take a string from the user and store it in a variable.
#2. Initialize a count variable to 0.
#3. Use a for loop to traverse through the characters in the string.
#4. Use an if statement to check if the character is a vowel or not and increment the count variable if it is a vowel.
#5. Print the total number of vowels in the string.
#6. Exit.


string = input()
c = 0
for i in range(len(string)):
  if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
    c = c + 1
print("Number of vowels are")
print(c)