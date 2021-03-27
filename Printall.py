#Q. 56:

#Print all(Lists and Tuples)

#Write a program to print all the combinations of entered numbers. The program consists of three numbers and print all the possible combinations.
#Refer sample input and output for formatting specification. 
#All float values are displayed correct to 2 decimal places. 
#All text in bold corresponds to input and the rest corresponds to output


T = list()
for i in range(3):
  T.append(int(input()))
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i!=j and j!=k and k!=i:
                print(T[i],T[j],T[k])