# Create a new Python file in this folder called “Strings.py” 
# Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog!” as a single string
# Now reprint this sentence as “The quick brown fox jumps over the lazy dog”  using the replace() function to change every “!” exclamation mark with a blank space.
# Now reprint that sentence as “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG. using the .upper() function
# Print the sentence in reverse.

# Save the sentence in a variable
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"

# Replace the ! with a space
sentence = sentence.replace("!"," ")

# Print out the sentence
print(sentence)

# Print out the sentence in upper case only
print(sentence.upper())

# Print out the sentence in reverse
print(sentence[::-1])