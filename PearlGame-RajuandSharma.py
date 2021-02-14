#Q. 15:

#Pearl Game - Raju and Sharma(Control Stmt - if-elif-el)

#Raju and his friend Sharma decided to collect pearls from beach as their hobby. Sharma and Raju started collecting the pearls from the beach and stored it in the repository.  Sharma was very happy as his friend Raju was doing it for so many days. 
#The people near the Raju and Sharmas house were so jealous about Raju-Sharma friendship as they were very intimate and collected pearls and stored it in the repository. 
#One day suddenly Sharma asked his friend Raju  and decided to count the number of pearls they collected for so long. 
#They started counting the pearls that has been stored in the repository. After collecting it Sharma and Raju decided to calculate the average pearls collected daily from the beach. Kindly help Sharma and Raju in calculating it.
#


T = int(input())
Num = []
s = 0
for i in range(T):
  Num.append(int(input()))
for i in range(T):
  s = s + Num[i]
avg = s//T
print(avg)