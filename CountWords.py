#Q. 92:

#Count Words(File Handling)

#Write a python program to create a file and display the count of all the characters in the file
#Hint:
#1. Create a File
#2. Take the input as number of lines to be written into the file
#3. Based on the number of lines get the input from the user
#4. File name to be searched
#Input:
#1. Filename
#2. The number of lines to be written into the file
#3. File name
#Output:
#Display the count of all characters in the file


name = input()
lines = int(input())
file = open(name,"w")
for i in range(0,lines):
  string = input()
  file.write(string)
file.close()
name = input()
file = open(name,"r")
n = file.read().replace(" ","")
res = ''.join([i for i in n if not i.isdigit()])
print(len(res))