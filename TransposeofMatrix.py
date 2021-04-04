#Q. 63:

#Transpose of Matrix(Matrix  Operations)

#Write a python program to create a NESTED LIST and print the diagonal elements of the matrix
#Hint:
#1. Input the number of rows First Matrix
#2. Input the number of Columns for first Matrix
#3. Display the elements of the matrix
#4. Display the transpose of the matrix


r = int(input())
c = int(input())
M = list()
for i in range(r):
  l = []
  for j in range(c):
    l.append(int(input()))
  M.append(l)
print("Given Matrix")
original = [[M[i][j] for j in range(len(M))] for i in range(len(M[0]))]
for n in original:
  print(n)
print("Transpose of the matrix")
result = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
for n in result:
   print(n)