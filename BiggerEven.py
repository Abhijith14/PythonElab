#Q. 23:

#Bigger Even(Control Stmt - for-while)

#Write a program to find the biggest even number from the given input
#Input:Positive numbers
#Output:Display the largest even number.
#Refer sample input and output for formatting specification.


T = int(input())
Num = []
maxi = 0
for i in range(T):
  Num.append(int(input()))
for i in range(T):
  if Num[i]%2 == 0:
    if Num[i] > maxi:
      maxi = Num[i]
print("Largest even number:",maxi)