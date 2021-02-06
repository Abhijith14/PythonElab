#Q. 7:

#Salary Calculator(Input and Output)

#Help Raja to calculate a first salary that he got from the organisation , he was confused with an salary credited in his account . 
#He asked his friend Ritu to identify how salary pay got calculated by giving the format of salary.
#His basic pay (to be entered by user) and Ritu developed a software to calculate the salary pay,with format given as below
#HRA=80% of the basic pay,
#dA=40% of basic pay
#bonus = 25 % of hra 
#Input and Output Format:
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output


BP = int(input())
HRA = (80*BP)/100
dA = (40*BP)/100
bonus = (25*HRA)/100
print("Total Salary=",BP+HRA+dA+bonus)