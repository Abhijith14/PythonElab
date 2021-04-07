#Q. 66:

#Identity Matrix(Matrix  Operations)

#Write a python program to create a NESTED LIST and print the identify matrix (without commas and brackets) 
#Hint:
#1. Input the number of rows and columns of the Square Matrix
#Output:
#Display the  identify matrix based on the input from the user


n = int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1")
        else:
            print("0")
  