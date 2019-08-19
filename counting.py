#   Import the Counter module
from collections import Counter

#   Get a string from user
string = input("Please enter a string: ")

#   Store string in a list
stringList = list(string)

#   Use Counter module to count the repetition of characters in list
count=Counter(stringList)
print(count)
