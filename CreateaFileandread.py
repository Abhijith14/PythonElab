#Q. 93:

#Create a File and read(File Handling)

#Write a python program to create a file and display the contents
#Hint:
#1. Create a File
#2. Take four inputs from the user and add the four lines to the file
#3. Display the contents of the file written in the output
#Input:
#1. Filename
#2,3,4,5 = File contents


name = input()
file = open(name,"w")
data1 = input()
data2 = input()
data3 = input()
data4 = input()
data = data1+data2+data3+data4
file.write(data)
file.close()
file = open(name,"r")
line = file.read()
print(line)
file.close()