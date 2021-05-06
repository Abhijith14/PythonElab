#Q. 95:

#Reverse File(File Handling)

#Write a Python Program to create a file and display the content(dynamic number of lines) and print the files contents in reverse order. 
#Hint 1:
#1. Create a file
#2. Take the Input as number of lines to be written into the file
#3. Based on the number of lines get the input from the user
#4. Get the file name from the user for performing operations
#5. Count the number of words in the file and display the number of words in the file input
#Input1:
#1: Filename
#2: The number of lines to be written into the file.
#3. File name to perform operations


name = input()
size = int(input())
file = open(name,"w")
for i in range(0,size):
  data = input()
  file.write(data+"\n")
file.close()
name = input()
for line in reversed(list(open(name))):
  print(line.rstrip())