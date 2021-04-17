#Q. 76:

#Display Items(Dictionary)

#Write a program to get four dictionary items and display all the key-values format using update function and items() function


D1 = {}
D2 = {}
D3 = {}
D4 = {}
k = int(input())
D1[k] = int(input())
k = int(input())
D2[k] = int(input())
k = int(input())
D3[k] = int(input())
k = int(input())
D4[k] = int(input())

print(list(D1.items()))
print(list(D2.items()))
print(list(D3.items()))
print(list(D4.items()))