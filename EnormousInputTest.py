#Q. 6:

#Enormous Input Test(Input and Output)

#The purpose of this problem is to verify whether the method you are using to read input data is sufficiently fast to handle problems branded with the enormous Input/Output warning. You are expected to be able to process at least 2.5MB of input data per second at runtime.
#Input
#The input begins with two positive integers n k (n, k<=10 power 7). The next n lines of input contain one positive integer ti, not greater than 10 power 9, each.
#Output
#Write a single integer to output, denoting how many integers ti are divisible by k.
#Example
#Input:
#7 3
#1
#51
#966369
#7
#9
#999996
#11
#Output:
#4


X = input().split()
N = int(X[0])
K = int(X[1])
ti = []
c = 0
for i in range(N):
  ti.append(int(input()))
for i in ti:
  if i % K == 0:
    c = c + 1
print(c)