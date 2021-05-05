#Q. 94:

#Find the word occurrence(File Handling)

#Write a python program to create a file and display the contents (dynamic number of lines) and count the occurrence of the word in the file and display the count.
#Hint:
#1. Create a File
#2. Take the input as number of lines to be written into the file
#3. Based on the number of lines get the input from the user
#4. Get the word to be searched in the file
#5. Display the count of the entered word in the file
#Input:
#1. Filename
#2. The number of lines to be written into the file
#3. word to be searched in the file content


name = input()
file = open(name,"w")
size = int(input())
for i in range(0,size):
  data = input()
  file.write(data)
file.close()
file = open(name,"r")
ele = input()
line = file.read()
c = line.count(ele)
print("Occurrences of the word")
print(c)
file.close()