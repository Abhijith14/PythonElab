#Q. 69:

#Matrix Display -Type 1(Matrix  Operations)

#Write a python program to create a NESTED LIST and form a matrix. 
#Hint:
#1. Input the number of rows and columns for First Matrix
#2. Input the number of rows and columns for Second Matrix
#3. Display the first matrix elements in Matrix format
#4. Display the first matrix elements in Matrix format


r = int(input())
c = int(input())
M1 = list()
M2 = list()
for i in range(r):
  l = []
  for j in range(c):
    l.append(int(input()))
  M1.append(l)
for i in range(r):
  l = []
  for j in range(c):
    l.append(int(input()))
  M2.append(l)
print("Matrix 1")
mat1 = [[M1[i][j] for j in range(len(M1))] for i in range(len(M1[0]))]
for n in mat1:
  print(n)
print("Matrix 2")
mat2 = [[M2[i][j] for j in range(len(M2))] for i in range(len(M2[0]))]
for n in mat2:
  print(n)