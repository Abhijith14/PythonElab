#Q. 45:

#Amicable(Functions)

#Write a python function to calculate whether the numbers are amicable or not
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output


def ami(num1,num2):
  s1 = s2 = 0
  for i in range(1,num1):
    if num1%i == 0:
      s1 = s1 + i
  for i in range(1,num2):
    if num2%i == 0:
      s2 = s2 + i
  if s1 == num2 and s2 == num1:
    print("Amicable")
  else:
    print("Not Amicable")
    
num1 = int(input())
num2 = int(input())
ami(num1,num2)