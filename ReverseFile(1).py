#Q. 100:

#Reverse File(File Handling)

#Write a python program to create a file and display the contents (dynamic number of lines) and print the files contents in reverse order.
#Hint:
#1. Create a File
#2. Take the input as number of lines to be written into the file
#3. Based on the number of lines get the input from the user
#4. Get the file name from the user for performing operations
#5. Count the number of words in the file and display the number of words in the fie
#Input:
#1. Filename
#2. The number of lines to be written into the file
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