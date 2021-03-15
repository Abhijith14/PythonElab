#Q. 44:

#Natural Numbers(Functions)

#Python Program to Find the Sum of First N Natural Numbers
#Input 
#Value of "N"
#Output
#Print the Sum of N natural Numbers


N = int(input())
s = 0
for i in range(1,N+1):
  s = s + i
print(s)