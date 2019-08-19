#   Import Match for the functionality
import math

#   Ask user for the amount he/she is depositing
P = float(input("Please enter the amount you are depositing? "))

#   Ask user for the interest rate
i = int(input("Please enter the interest rate: "))
i = i/100

#   Ask user for the number of years to leave the deposit
t = int(input("Please enter how many years you want to leave your deposit for? "))

#   Ask user if he/she wants simple or compound interest
interest = input("Do you want simple or compound interest? ")
if interest == "simple":
    interestSimple = round((P*(1+i*t)),2)
    print(f"You will have {interestSimple}")
elif interest == "compound":
    interestCompound = round((P* math.pow((1+i),t)),2)
    print(f"You will have {interestCompound}")
else:
    interest = input("You must choose either simple or compound? ")
