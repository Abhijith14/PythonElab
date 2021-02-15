#Q. 16:

#Grade(Control Stmt - if-elif-el)

#Write a program asks the user to enter a exam score, and then prints the grade (A/B/C/D) that corresponds to the score. 
#If the score that the user entered is less than 0 or greater than 100, the program prints an error message.
#Use the following grades
#A grade >=85
#B grade   70-85
#C grade  50-70
#D grade <50


score = int(input())
if score >= 85:
  print("A")
elif score > 70 and score < 85:
  print("B")
elif score > 50 and score < 70:
  print("C")
elif score < 50:
  print("D")