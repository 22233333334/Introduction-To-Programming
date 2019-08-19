#   Ask user for a sentence
sentence = input("Please enter a sentence: ")

#   Ask user which characters they would like removed
charactersRemove = input("Which characters would you like removed? ")

#   Create a for loop to check what character to remove in sentence and replace with a blank
for i in charactersRemove:
    sentence = sentence.replace(i,'')
    sentence = sentence
print (sentence)
