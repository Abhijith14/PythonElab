#Q. 10:

#Village Homes(Input and Output)

#There are n villages in a line in an area. There are two kinds of tribes A and B that reside there. A village can be either empty or occupied by one of the tribes. An empty village is said to be controlled by a tribe of village A if it is surrounded by villages of tribes A from the left and from the right. Same goes for the tribe B.
#Find out the number of villages that are either occupied by or controlled by tribes A and B, respectively.
#Input
#The first line of the input contains an integer T denoting the number of test cases.
#The first line of the input contains a string s denoting the configuration of the villages, each character of which can be 'A', 'B' or '.'.
#Output
#For each test case, output two space-separated integers denoting the number of villages either occupied by or controlled by tribe A and B, respectively.
#Constraints
#1<= T<=20
#1<=|s|<=105
#Subtasks
#Subtask #1 (40 points): 1<= |s| <= 103
#Subtask #2 (60 points): Original constraints
#Example
#Input
#4
#A..A..B...B
#..A..
#A....A
#..B..B..B..
#Output
#4 5
#1 0
#6 0
#0 7


x = int(input())
for _ in range(x):
    u = input()
    f = 100
    a = 0
    b = 0
    c = 0
    for i in u:
        if i == 'A':
            if f == 0:
                b += a
            f = 0
            a = 0
            b += 1
        elif i == 'B':
            if f == 1:
                c += a
            f = 1
            a = 0
            c += 1
        elif i == '.':
            a += 1
    print(b, c)