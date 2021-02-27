#Q. 28:

#Exponentation- Part B(Control Stmt - for-while)

#Write a program to find the exponentation of given number
#Input 1: Base
#Input 2: Number of inputs
#Output:
#List of exponentation terms for the given input


exp = int(input())
no = int(input())
print("The total terms is:",no)
i,s = 1,1
print(1)
while i <= no:
  s = s*exp
  print(s)
  i = i + 1