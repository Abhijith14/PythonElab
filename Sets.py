#Q. 26:

#Sets(Control Stmt - for-while)

#Write a program to do basic set operations
#Input:Two Sets
#Output:
#Result of Union,intersection,difference and symmetric difference operations on the given input
#Refer sample input and output for formatting specification.


l1 = int(input())
l2 = int(input())
s1 = []
s2 = []
U = []
I = []
D = []
f = 0
for i in range(l1):
  s1.append(int(input()))
for i in range(l2):
  s2.append(int(input()))

for i in range(l1):
  U.append(s1[i])
for i in range(l2):
  U.append(s2[i])
U = list(dict.fromkeys(U))  

for i in range(l1):
  for j in range(l2):
    if s1[i] == s2[j]:
      I.append(s1[i])

for i in range(l1):
  for j in range(l2):
    if s1[i] != s2[j]:
      f = 1
    else:
      f = 0
      break
  if f == 1:
    D.append(s1[i])
      
print(s1)
print(s2)
print("Union is: {",end = "")
for i in range(len(U)):
  if i < len(U)-1:
    print(U[i],end = ", ")
  else:
    print(U[i],end = "}")
print()
print("Intersection is {",end = "")
for i in range(len(I)):
  if i < len(I)-1:
    print(I[i],end = ", ")
  else:
    print(I[i],end = "}")
print()
print("Difference is {",end = "")
for i in range(len(D)):
  if i < len(D)-1:
    print(D[i],end = ", ")
  else:
    print(D[i],end = "}")