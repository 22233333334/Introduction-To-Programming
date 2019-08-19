#   Add function for adding
def addNum(a,b):
    return a + b

#   Add function to subtract
def subtractNum(a,b):
    return a - b

#   Add function to multiply
def multiplyNum(a,b):
    return a * b

#   Add function to divide
def divideNum(a,b):
    return a/b

#   Create function of options for user to choose
def options():
    print("Options: ")
    print("Option 1 - add")
    print("Option 2 - subtract")
    print("Option 3 - multiply")
    print("Option 4 - divide")
    print("Option 5 - exit")
    print("")

#   Create empty variable for choice and show options
choice = ""
options()

#   Use while loop to give user the options until he / she quits the program
while choice != "5":
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        a = float(input("Please enter the first number to add: "))
        b = float(input("Please enter the second number to add: "))
        print(f"The sum is {addNum(a,b)}")
    elif choice == 2:
        a = float(input("Please enter the first number: "))
        b = float(input("Please enter the second number to subtract from the first number: "))
        print(f"The subtraction would be {subtractNum(a,b)}")
    elif choice == 3:
        a = float(input("Please enter the first number: "))
        b = float(input("Please enter the second number: "))
        print(f"Multiplying the two numbers would give you {multiplyNum(a,b)}")
    elif choice == 4:
        a = float(input("Please enter the first number: "))
        b = float(input("Please enter the second number: "))
        print(f"Dividing the second number from the first number would give you {divideNum(a,b)}")
    elif choice == 5:
        print("You have exited the program.")
        break
    else:
        print("We don't recognize that choice.")
        options()
