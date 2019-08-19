#   Declare boolean for length of password
haveLength = False

#   Declare boolean for uppercase letters of password
upCase = False

#   Declare boolean for lowercase letters of password
lowCase = False

#   Declare boolean for containing of numbers in password
haveNum = False

#   Declare variable for counts of True to be added
requirementsMet = 0

#   Ask user for length of password and check if yes (increase by 1), if no (do nothing)
lengthPassword = input("Is your password more than 6 characters? (Yes or No) ")
if lengthPassword == "Yes":
    haveLength = True
    requirementsMet +=1

#   Ask user if password has uppercase letters and check if yes (increase by 1), if no (do nothing)
upperPassword = input("Does your password have uppercase letters? (Yes or No) ")
if upperPassword == "Yes":
    upCase = True
    requirementsMet +=1

#   Ask user if password has lowercase letters and check if yes (increase by 1), if no (do nothing)
lowerPassword = input("Does your password have lowercase letters? (Yes or No) ")
if lowerPassword == "Yes":
    lowCase = True
    requirementsMet +=1

#   Ask user if there are numbers in the password and check if yes (increase by 1), if no (do nothing)
numbersPassword = input("Does your password have numbers? (Yes or No) ")
if numbersPassword == "Yes":
    haveNum = True
    requirementsMet +=1

#   Check how many requirements have been met
if requirementsMet == 3:
    print("This is a suitable password.")
else:
    print("The password does not meet the minimum requirements.")