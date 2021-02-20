#Q. 21:

#FACTORS(Control Stmt - for-while)

#The program finds the factors of a number, which means the other numbers which can divide the given number.       
#Eg: 5 is divisible by 5 and 1


num = int(input())
for i in range(2,num+1):
  if num%i == 0:
    print(i)
print("1")