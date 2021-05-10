#Q. 99:

#Create a dynamic file and read(File Handling)

#Write a python program to create a file and display the contents (dynamic number of lines)
#Hint:
#1. Create a File
#2. Take the input as number of lines to be written into the file
#3. Based on the number of lines get the input from the user
#4. Add a new line to the file after each input.
#5. Display the contents of the file written in the output
#Input:
#1. Filename
#2,3,4,5 = File contents


name = input()
size = int(input())
file = open(name,"w")
for i in range(0,size):
  data = input()
  if i == size-1:
    file.write(data + "\n")
  else:
    file.write(data + "\n\n")
file.close()
file = open(name,"r")
n = file.read()
print(n)
print("Number of lines:")
print(size*2)