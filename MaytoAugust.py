#Q. 17:

#May to August(Control Stmt - if-elif-el)

#The length of a month varies from 30 and 31 days. 
#In this exercise you will create a program that reads the name of a month from the user as a string. 
#The program should get input from May to August.
#If the input is from may to other months then display error messages as "Invalid"


a=str(input())
if a=="May":
    print(31)
elif a=="Jun":
    print(30)
elif a=="Jul":
    print(31)
elif a=="Aug":
    print(30)
else:
    print("Invalid")