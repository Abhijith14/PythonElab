#Q. 65:

#Spirally traversing a matrix(Matrix Operations)

#Traverse a 4x4 matrix of integers in spiral form.
#Input: The first line of input contains an integer T denoting the number of test cases. First four lines of the test case will contain four elements each.
#Output: Spiral array will be displayed in a single line.
#Constraints:
#1 <=T<= 100
#1 <=N<= 100


T = int(input())
for i in range(T):
  R = []
  R1 = []
  R2 = []
  R3 = []
  R4 = []
  t1 = input().split()
  t2 = input().split()
  t3 = input().split()
  t4 = input().split()
  for j in range(len(t1)):
    R1.append(int(t1[j]))
  for j in range(len(t2)):
    R2.append(int(t2[j]))
  for j in range(len(t3)):
    R3.append(int(t3[j]))
  for j in range(len(t4)):
    R4.append(int(t4[j]))
  for j in range(len(R1)):
    R.append(R1[j])
  R.append(R2[-1])
  R.append(R3[-1])
  R4.reverse()
  for j in range(len(R4)):
    R.append(R4[j])
  R.append(R3[0])
  for j in range(len(R2)-1):
    R.append(R2[j])
  R.append(R3[2])
  R.append(R3[1])
  print(R)