#Q. 39:

#Check the Functions(Strings)

#Write a program to check whether the given string contains the following:
#1. input.isalpha()   = check if all char in the string are alphabetic
#2. input.isdigit()     = test if string contains digits
#3. input.istitle()      = test if string contains title words
#4. input.isupper()  = test if string contains upper case
#5. input.islower()   = test if string contains lower case


string = input()
a = b = c = d = e = False 
for i in range(len(string)):
  if str.isalpha(string[i]):
    a = True
  if str.isdigit(string[i]):
    b= True
  elif str.istitle(string):
    c = True
  elif str.isupper(string[i]):
    d = True
  elif str.islower(string[i]):
    e = True
print(a)
print(b)
print(c)
print(d)
print(e)