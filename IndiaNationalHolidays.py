#Q. 11:

#India National Holidays(Control Stmt - if-elif-el)

#Date to Holiday Name
#India has three national holidays which fall on the same dates each year.
#Holiday Date
#New Year January 1
#Independence  Day August 15 
#Republic DayJanuary 26
#Write a program that reads a month and day from the user. If the month and day match one of the holidays listed previously then your program should display the holidays name. 
#Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday. 
#India has two additional national holidays, Good Friday and Labour Day, whose dates vary from year to year. There are also numerous provincial and territorial holidays, some of which have fixed dates, and some of which have variable dates. 
#We will not consider any of these additional holidays in this exercise.


m = input()
d = int(input())
if m == 'January':
  if d == 1:
    print("New Year")
  elif d == 26:
    print("Republic Day")
  else:
    print("Sorry No National Holidays");
elif m == 'August':
  if d == 15:
    print("Independence Day")
  else:
    print("Sorry No National Holidays")
else:
  print("Sorry No National Holidays")

	