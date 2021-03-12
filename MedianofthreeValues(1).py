#Q. 41:

#Median of three Values(Functions)

#Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median.
#Hint: The median value is the middle of the three values when they are sorted into ascending order. It can be found using if statements, or with a little bit of mathematical creativity
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output


import statistics
def med_calc(a,b,c):
  seq = []
  seq.append(a)
  seq.append(b)
  seq.append(c)
  print(statistics.median(seq))
  
x = int(input())
y = int(input())
z = int(input())
med_calc(x,y,z)