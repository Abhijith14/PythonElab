#Q. 49:

#Prime Numbers(Functions)

#Python Program to Print all the Prime Numbers within a Given Range
#Input :
#Upper Limit
#Output :
#Print the prime numbers within the specified limit


n = int(input())
for i in range(2,n+1):
  c=0;
  for j in range(1,i+1):
    if i % j == 0:
      c = c + 1
  if(c==2):
    print(i)
    