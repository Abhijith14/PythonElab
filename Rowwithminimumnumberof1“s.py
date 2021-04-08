#Q. 67:

#Row with minimum number of 1's(Matrix Operations)

#Determine the row index with minimum number of ones. The given 2D matrix has only zeroes and ones and also the matrix is sorted row wise . If two or more rows have same number of 1's than print the row with smallest index.
#Note: If there is no '1' in any of the row than print '-1'.
#Input:
#The first line of input contains an integer T denoting the number of test cases. The first line of each test case consists of two integer n and m. The next line consists of n*m spaced integers. 
#Output:
#Print the index of the row with minimum number of 1's.
#Constraints: 
#1<=T<=200
#1<=n,m<=100


t = int(input())
z=0
while z < t :
    m,n = map(int,input().split())
    arr=list(map(int,input().split()))
    mi=-1
    s=111111
    for i in range(m) :
        if sum(arr[i*n:i*n+n])<s and sum(arr[i*n:i*n+n])!=0 :
            mi=i
            s=sum(arr[i*n:i*n+n])
    if sum(arr)==0 :
        print("minus1")
    else:
        print(mi)
    z=z+1