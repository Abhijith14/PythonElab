#Q. 20:

#Seasoners(Control Stmt - if-elif-el)

#The year is divided into four seasons: spring, summer, fall and winter. While the exact dates that the seasons change vary a little bit from year to year because of the way that the calendar is constructed, we will use the following dates for this exercise:
#Season First day
#Summer March 20
#Spring  June 21
#Fall September 22
#Winter December 21                  
#Create a program that reads a month and day from the user. The user will enter the name of the month as a string, followed by the day within the month as an integer. 
#Then your program should display the season associated with the date that was entered. 
#Note: Enter First three letter for month example: Jan for january, Feb for Feburary ans so on....and first letter of the month should be capital


m = input()
d = int(input())
S = 'null'
f = 0
dictM = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
Summer = [3,4,5,6]
Spring = [6,7,8,9]
Fall = [9,10,11,12]
Winter = [12,1,2,3]

#Summer

for n in range(4):
  if dictM[m] == Summer[n]:
    if dictM[m] == 3 and d >= 20:
      S = "Summer"
      f = 1
    elif dictM[m] > 3 and dictM[m] < 6:
      S = "Summer"
      f = 1
    elif dictM[m] == 6 and d < 21:
      S = "Summer"
      f = 1
      
#Spring
      
for n in range(4):
  if dictM[m] == Spring[n] and f == 0:
    if dictM[m] == 6 and d >= 21:
      S = "Spring"
      f = 1
    elif dictM[m] > 6 and dictM[m] < 9:
      S = "Spring"
      f = 1
    elif dictM[m] == 9 and d < 22:
      S = "Spring"
      f = 1
      
#Fall
      
for n in range(4):
  if dictM[m] == Fall[n] and f == 0:
    if dictM[m] == 9 and d >= 22:
      S = "Fall"
      f = 1
    elif dictM[m] > 9 and dictM[m] < 12:
      S = "Fall"
      f = 1
    elif dictM[m] == 12 and d < 21:
      S = "Fall"
      f = 1
      
#Winter
      
for n in range(4):
  if dictM[m] == Winter[n] and f == 0:
    if dictM[m] == 12 and d >= 21:
      S = "Winter"
      f = 1
    elif dictM[m] < 3:
      S = "Winter"
      f = 1
    elif dictM[m] == 3 and d < 20:
      S = "Winter"
      f = 1

print(S)