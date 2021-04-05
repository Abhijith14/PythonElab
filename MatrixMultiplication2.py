#Q. 64:

#Matrix Multiplication 2(Matrix  Operations)

#Write a program for matrix multiplication


r1 = int(input())
c1 = int(input())
A = list()
B = list()
C = list()
l = list()
for i in range(r1):
  l = []
  for j in range(c1):
    l.append(int(input()))
  A.append(l)
r2 = int(input())
c2 = int(input())
for i in range(r2):
  l = []
  for j in range(c2):
    l.append(int(input()))
  B.append(l)
C = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
for i in range(len(C)):
  print(C[i])
    