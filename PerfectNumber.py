#Q. 22:

#Perfect Number(Control Stmt - for-while)

#Write a program to check whether the given number is perfect number or not
#Input:A positive number
#Output:Display the appropriate message 
#Refer sample input and output for formatting specification.


num = int(input())
s = 0
for i in range(1,num):
  if num % i == 0:
    s = s + i
if s == num:
  print("The number is a Perfect number")
else:
  print("The number is not a Perfect number")