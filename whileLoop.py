#   Create list to store incorrect inputs and the correct name
incorrectInput = []
correctName = "John"

#   Ask for user input with a while loop to store incorrect inputs
userInput = input("Please enter your name: ")

while userInput != correctName:
    incorrectInput.append(userInput)
    userInput = input("Please enter the correct name: ")
print(f"Incorrect names: {incorrectInput}")


