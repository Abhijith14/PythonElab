#Q. 43:

#Solve Equation(Functions)

#Python Program to Find the Sum of the Series: 1 + 1/2 + 1/3 + .. + 1/N
#Input:
#The number of terms
#Output
#Print the Sum of Series


num = int(input())
s = 1
for i in range(2,num+1):
  s = s + (1/i)
print("",'%.2f'%s)