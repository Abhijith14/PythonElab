#Q. 47:

#Shipping Calculator(Functions)

#An online retailer provides express shipping for many of its items at a rate of 750 for the first item, and 200 for each subsequent item. Write a function that takes the number of items in the order as its only parameter. 
#Return the shipping charge for the order as the functions result. Include a main program that reads the number of
#items purchased from the user and displays the shipping charge.
#Refer sample input and output for formatting specification.
#All float values are displayed correct to 2 decimal places.
#All text in bold corresponds to input and the rest corresponds to output


def price(N):
  s = 750
  for i in range(2,N+1):
    s = s + 200
  return s

def main():
  num = int(input())
  print(price(num))

  
if __name__ == '__main__':
  main()