#Q. 3:

#Sum of the Series(Input and Output)

#Write a program to find sum of series
#Hint:1+2+3+4+n


n = int(input())
i = 1
s = 0
while i <= n:
  s = s + i
  i+=1
print(s)