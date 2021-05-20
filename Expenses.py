#Q. 9:

#Expenses(Input and Output)

#While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. 
#If the quantity and price per item are input, write a program to calculate the total expenses.
#Input
#The first line contains an integer T, total number of test cases. Then follow T lines, each line contains integers quantity and price.
#Output
#Output the total expenses while purchasing items.
#Constraints
#1<=T<=1000
#1<=quantity, price <=100000
#Example
#Input
#3 
#100 120
#10 20
#1200 20
#Output
#12000.000000
#200.000000
#21600.000000


T = int(input())
for i in range(T):
  X = input().split()
  Q = int(X[0])
  P = int(X[1])
  F = Q * P
  if Q > 1000:
    N = F * 0.1
    F = F - N
  print('%0.6f'%float(F))