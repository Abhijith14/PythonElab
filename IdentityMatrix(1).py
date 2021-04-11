#Q. 70:

#Identity Matrix(Matrix  Operations)

#Write Python Program to read a number n and print an identity matrix of the desired size.
#Input:
#Size of the matrix
#Output:
#Print the Identity matrix


n = int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep = " ",end = " ")
        else:
            print("0",sep = " ",end = " ")
    print()
     
  