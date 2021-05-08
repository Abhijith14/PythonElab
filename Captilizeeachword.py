#Q. 97:

#Captilize each word(File Handling)

#Write a python program to create a file and Capitalise  each word (Starting letter) in the file
#Hint:
#1. Create a File
#2. Take the input as number of lines to be written into the file
#3. File name to be searched
#Input:
#1. Filename
#2. The number of lines to be written into the file
#3. File name
#Output:
#Display the file content with capitalise of each word (Starting letter)


name = input()
size = int(input())
file = open(name,"w")
for i in range(0,size):
  data = input()
  file.write(data+"\n\n")
file.close()
name = input()
file = open(name,"r")
n = file.read().title()
print(n)