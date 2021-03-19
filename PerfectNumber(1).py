#Q. 48:

#Perfect Number(Functions)

#Write a Python Program to Check if a Number is a Perfect Number


def perfect(num):
  s = 0
  for i in range(1,num):
    if num % i == 0:
      s = s + i
  if s == num:
    return("The number is a Perfect number!")
  else:
    return("The number is not a Perfect number!")

def main():
  num = int(input())
  print(perfect(num))

if __name__ == '__main__':
  main()