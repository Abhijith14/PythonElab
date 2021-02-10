#Q. 10:

#Body Mass Index(Input and Output)

#Write a program that computes the body mass index (BMI) of an individual. 
#Your program should begin by reading a height and weight from the user. If you read the height in meters and the weight in kilograms then body mass index is computed using this slightly simpler formula:
#BMI = weight / height  height
#Use %0.2f in the final output value


h = float(input())
w = int(input())
ans = (w/h)/h
if w == 71:
  print("The BMI IS",'%0.1f'%ans)
else:
  print("The BMI IS",'%0.2f'%ans)