#   Create variable to save all contents of text file
contents = ""

#   Open file in read only mode
f = open("input.txt", "r")

#   Read all contents and save to contents
for line in f:
       contents = contents + line

#   Close the file
f.close()

#   Save number of lines in variable
numberLines = contents.count("\n")

#   Save number of characters in variable
numberCharacters = len(contents)

#   Save number of words in variable
numberWords = len(contents.split())

#   Declare variables to store how many times the character appears in the contents
countA = 0
countE = 0
countI = 0
countO = 0
countU = 0

#   Had to declare this character so that I don't get an error in the else condition, so I'm catching those extra characters to be counted?
countExtra = 0

#   Use for loop to count the number of occurences the specific character appears
for i in contents:
    if i == "a": 
        countA +=1
    elif i == "e":
        countE +=1
    elif i == "i":
        countI +=1
    elif i == "o":
        countO +=1
    elif i == "u":
        countU +=1
    else:
        countExtra +=1

print(f"Number of characters are: {numberCharacters}.\nNumber of words are: {numberWords}.\nNumber of lines are: {numberLines}.\n")
print(f"Number of times the vowel appears:\nA: {countA}\nE: {countE}\nI: {countI}\nO: {countO}\nU: {countU}")