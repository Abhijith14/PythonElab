#Q. 29:

#Sum of Squares of Each Digit(Control Stmt - for-while)

#Write a program to read a positive integer and find the sum of squares of individual digits.


def sum_of_squares_of_digits(value):
    return sum(int(c) ** 2 for c in str(value))
N = int(input())
print(sum_of_squares_of_digits(N))