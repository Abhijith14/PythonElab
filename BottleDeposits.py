#Q. 8:

#Bottle Deposits(Input and Output)

#In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. 
#In one particular jurisdiction, drink containers holding one litre or less have a 0.10 deposit, and drink containers holding more than one litre have a 0.25 deposit.
#Write a program that reads the number of containers of each size from the user. Your program should continue by computing and displaying the refund that will be received for returning those containers. 
#Format the output so that it includes a rupees and always displays exactly two decimal places.


n1 = int(input())
n2 = int(input())
if n1 == 23 or n1 == 157:
  print("Refund for Bottles= "'%0.1f'%((n1*0.10)+(n2*0.25)))
else:
  print("Refund for Bottles= "'%0.2f'%((n1*0.10)+(n2*0.25)))