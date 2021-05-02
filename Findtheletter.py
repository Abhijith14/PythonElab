#Q. 91:

#Find the letter(File Handling)

#Write a python program to create a file and display the contents (dynamic number of lines) and count the occurrence of the letter in the file and display the count.
#Hint:
#1. Create a File
#2. Take the input as number of lines to be written into the file
#3. Based on the number of lines get the input from the user
#4. Input the file name to perform the operations
#5. Input the letter to be searched in the file
#Input:
#1. Filename
#2. The number of lines to be written into the file
#3. File name
#4. Letter to be searched
#Output:
#The occurrence(count) of the letter


name = input()
file = open(name,"w")
size = int(input())
for i in range(0,size):
  data = input()
  file.write(data + "\n")
file.close()
name = input()
file = open(name,"r")
ele = input()
line = file.read()
c = line.count(ele)
print("Occurrences of the letter")
print(c)
file.close()