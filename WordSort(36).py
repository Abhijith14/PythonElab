#Q. 30:

#Word Sort(Control Stmt - for-while)

#Write a program to sort the words in the sentence in alphabetic order
#Input:A Sentence 
#Output: Display the words of a sentence in sorted order 
#Refer sample input and output for formatting specification.


string = input()
data = {}
lst = list(string.split(" "))
for i in range(len(lst)):
  data.update({lst[i][0]:lst[i]})
print("The sorted words are")
for i in sorted (data.keys()):
  print(data[i]) 