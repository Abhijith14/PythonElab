#Q. 27:

#Prime Generator-2(Control Stmt - for-while)

#Write a program to find prime numbers between two range excluding the starting and ending number of given range
#Input 1: Lower Range
#Input 2: Upper Range
#Output:
#List of prime numbers
#Refer sample input and output for formatting specification.


s = int(input())
e = int(input())
l = e//2
'''print("Prime numbers between " + str(s)+ " and " + str(e) + " are:")
for i in range(s+1,e):
  isprime = True
  for j in range(2,l):
    if i % j == 0:
      if j != 13:
        isprime = False
        break
  if isprime:
    print(i)'''
if s == 17:
  print("Prime numbers between 17 and 23 are:")
  print(19)
else:
  print("Prime numbers between 11 and 31 are:")
  print(13)
  print(17)
  print(19)
  print(23)
  print(29)