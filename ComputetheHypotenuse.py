#Q. 46:

#Compute the Hypotenuse(Functions)

#Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the functions result. 
#Include a main program that reads the lengths of the shorter sides of a right triangle from the user, uses your function to compute the length of the hypotenuse, and displays the result.
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output


import math
def hyp(a,b):
	return int(math.sqrt(b**2+a**2))
def main():
  b = int(input())
  a = int(input())
  print(hyp(a,b))
  
if __name__ == '__main__':
  main()