#Q. 2:

#SRM Salary Work(Input and Output)

#In a company an employee is paid as under: If his basic salary is less than Rs. 1500, then HRA = 10% of base salary and DA = 90% of basic salary. 
#If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the Employee's salary is input, write a program to find his gross salary. 
#NOTE: Gross Salary = Basic Salary+HRA+DA
#Input
#The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer salary.
#Output
#Output the gross salary of the employee.
#Constraints
#1<=T<=1000
#1<=salary<=100000


T = int(input())
for x in range(T):
  basic = int(input())
  if basic < 1500:
    HRA = 0.1 * basic
    DA = 0.9 * basic
  elif basic >= 1500:
    HRA = 500
    DA = 0.98 * basic
  gross = basic + HRA + DA
  print(gross)
    