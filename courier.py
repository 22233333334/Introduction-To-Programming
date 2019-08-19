#   Declare all variables to be used below
packageInsurance = 0
packageGiftPrice  = 0
packageImportance = 0

#   Ask user for price of package
packagePrice = float(input("Please enter the price of the package: "))

#   Ask user for total distance of delivery
packageDistance = int(input("What is the total distance for the package to be delivered in km's? "))

#   Ask user how package is to be delivered and calculate costs
deliveryMethod = input("How will the package be delivered? (air or freight) ")
if deliveryMethod == "air":
    deliveryCost = packageDistance * 0.36
elif deliveryMethod == "freight":
    deliveryCost = packageDistance * 0.25

#   Ask user for insurance to use and calculate costs
packageInsure = input("What insurance would you like? (full or limited) ")
if packageInsure == "full":
    packageInsurance = 50
elif packageInsure == "limited":
    packageInsurance = 25

#   Ask user to include gift or not
packageGift = input("Would you like to add a gift? (yes or no) ")
if packageGift == "yes":
    packageGiftPrice = 15
elif packageGift == "no":
    packageGiftPrice = 0

#   Ask user how important delivery is
packagePriority = input("How important is the delivery? (priority or standard) ")
if packagePriority == "priority":
    packageImportance = 100
elif packagePriority == "standard":
    packageImportance = 20

#   Add all costs together in a variable and print out to user
packageTotal = round((packagePrice + deliveryCost + packageInsurance + packageGiftPrice + packageImportance),2)
print(f"The total cost of the package based on your choices is R{packageTotal}")
