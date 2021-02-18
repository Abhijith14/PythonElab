#Q. 19:

#Name of the Shape(Control Stmt - if-elif-el)

#Write a program that determines the name of a shape from its number of sides. 
#Read the number of sides from the user and then report the appropriate name as part of a meaningful message. 
#Your program should support shapes with anywhere from 3 up to (and including) 6sides. 
#If a number of sides outside of this range is entered then your program should display an appropriate error message.
#1. If the input is 5 then display as  Pentagon 
#2. if the input is 6 display as Hexagon
#3.if the input is any another number then display the message "Input should be from 3 to 6"


num = input()
if num == '3':
  print("Triangle")
elif num == '4':
  print("Quadrilateral")
elif num == '5':
  print("Pentagon")
elif num == '6':
  print("Hexagon")
else:
  print("Input should be from 3 to 6")