#Q. 62:

#Overlapping rectangles(Matrix Operations)

#Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y co-ordinates of two points: the left top corner and the right bottom corner of the rectangle.
#Note that two rectangles sharing a side are considered overlapping.
#rectanglesOverlap
#Input:
#The first integer T denotes the number of test cases. For every test case, there are 2 lines of input. The first line consists of 4 integers: denoting the co-ordinates of the 2 points of the first rectangle. The first integer denotes the x co-ordinate and the second integer denotes the y co-ordinate of the left topmost corner of the first rectangle. The next two integers are the x and y co-ordinates of right bottom corner. Similarly, the second line denotes the cordinates of the two points of the second rectangle.
#Output:
#For each test case, output (either 1 or 0) denoting whether the 2 rectangles are overlapping. 1 denotes the rectangles overlap whereas 0 denotes the rectangles do not overlap.
#Constraints:
#1 <= T <= 10
#-10000 <= x,y <= 10000
#T denotes the number of test cases. x denotes the x co-ordinate and y denotes the y co-ordinate.


s = int(input())
for i in range(s):
  f = 1
  R1 = []
  R2 = []
  t1 = input().split()
  t2 = input().split()
  for j in range(len(t1)):
    R1.append(int(t1[j]))
  for j in range(len(t2)):
    R2.append(int(t2[j]))
  if R1[0] >= R2[2] or R2[0] >= R1[2]:
    f = 0
  if R1[1] <= R2[3] or R2[1] <= R1[3]:
    f = 0
  print(f)
  