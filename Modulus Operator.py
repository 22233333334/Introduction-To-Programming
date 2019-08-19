# Create a Python file called "Optional_task" in this folder.
# This program should test whether a number is odd or even 
# Ask the user to enter an integer
# Test whether the number entered is odd or even 
# Print out the number and whether it is odd or even

#   Ask user for a whole number
user_Number = int(input("Please enter a whole number: "))

# Check if the number is odd or even
if user_Number % 2 == 0:
    print("Number is even")
elif user_Number % 2 == 1:
    print("Number is odd")


