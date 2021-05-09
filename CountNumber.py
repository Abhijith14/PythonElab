#Q. 98:

#Count Number(File Handling)

#Write a python program to create a file and display the contents (dynamic number of lines) and count the numbers in the file and display the count.
#Hint:
#1. Create a File
#2. Take the input as number of lines to be written into the file
#3. Based on the number of lines get the input from the user
#4. Input the file name to perform the operations
#Input:
#1. Filename
#2. The number of lines to be written into the file
#3. File name
#Output:
#The total count of the numbers in the file


def spliter(data):
  return list(data)

name = input()
size = int(input())
file = open(name,"w")
for i in range(0,size):
  data = input()
  file.write(data + "\n")
file.close()
c = 0
name = input()
file = open(name,"r")
data = file.read()
data = str(data).split()
l = len(data)
for i in range(0,l):
  res = spliter(data[i])
  for j in res:
    if j.isdigit() and j != 0:
      c = c + 1
print(c)