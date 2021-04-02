#Q. 61:

#Matrix Addition(Matrix  Operations)

#Write a python program to create a NESTED LIST and add the two matrix. (Without Square Brackets)
#Hint:
#1. Input the number of rows and columns for First Matrix
#2. Input the number of rows and columns for Second Matrix
#3. Display the first matrix elements in Matrix format (Without commas and Square Bracket)
#4. Display the first matrix elements in Matrix format (Without commas and Square Bracket)
#5. Display the result of sum of two matrix (Without commas and Square Bracket)


r1 = c1 = int(input())
r2 = c2 = int(input())
A = list()
B = list()
C = list()
l = list()
for i in range(r1):
  l = []
  for j in range(c1):
    l.append(int(input()))
  A.append(l)
for i in range(r2):
  l = []
  for j in range(c2):
    l.append(int(input()))
  B.append(l)
for i in range(r1):
  for j in range(c1):
    C.append(A[i][j]+B[i][j])
print("Matrix 1")
for i in range(r1):
  for j in range(c1):
    print(A[i][j]) 
print("Matrix 2")
for i in range(r2):
  for j in range(c2):
    print(B[i][j])
print("Sum of Matrix")
for i in range(len(C)):
  print(C[i])
    