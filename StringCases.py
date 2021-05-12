#Q. 1:

#String Cases(Input and Output)

#Chef has just found a recipe book, where every dish consists of exactly four ingredients. He is going to choose some two dishes and prepare them for dinner. Of course, he likes diversity and wants to know whether the two dishes are similar.
#Two dishes are called similar if at least half of their ingredients are the same. In other words, at least two of four ingredients of the first dish should also be present in the second dish. The order of ingredients doesn't matter.
#Your task is to examine T pairs of dishes. For each pair, check if the two dishes are similar and print "similar" or "dissimilar" accordingly.
#Input
#The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
#The first line of each test case contains four distinct strings, denoting ingredients needed for the first dish. Each ingredient is represented by a string of length between 2 and 10 inclusive, consisting of lowercase English letters.
#The second line of each test case describes the second dish in the same format.
#Output
#For each test case, output a single line containing the answer  "similar" if at least half of the ingredients are same, and "dissimilar" otherwise (without the quotes).
#Constraints
#1<=T<=200
#The length of each string will be between 2 and 10 inclusive.


T = int(input())
for x in range(T):
  f = 0
  c = 0
  d1 = input().split()
  d2 = input().split()
  for i in d1:
    for j in d2:
      if i == j:
        c = c + 1
        if c == 2:
          f = 1
          break
      else:
        f = 0
    if f == 1:
      break
  if f == 1:
    print("similar")
  else:
    print("dissimilar")
      