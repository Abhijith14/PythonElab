#Q. 25:

#Range Armstrong(Control Stmt - for-while)

#Write a program to find the armstrong numbers between the given range
#Input 1:Lower Range
#Input 2: Upper range
#Output:
#List of Armstrong numbers
#Refer sample input and output for formatting specification.


def finder(temp):
  s = 0
  while temp > 0:
    rem = temp%10
    s = rem**len(str(i)) + s
    temp = temp//10
  return s

l = int(input())
u = int(input())
i = l
for i in range(l,u+1):
  temp = i
  s = finder(temp)
  if i == s:
    print(i)
  i+=1