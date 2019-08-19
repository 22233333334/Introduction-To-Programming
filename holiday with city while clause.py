#   Ask user the following questions to calculate the total holiday cost
nightsNumber = int(input("Please enter how many nights you want to stay at the hotel for? "))
rentalPrice = int(input("Please enter for how many days you would like to rent out the car? "))
city = input("Please enter city that you want to fly to? (Port Elizabeth, Cape Town, Durban)")

#   Create function for Hotel cost
def hotelCost(nightsNumber):
    nightsNumber = float(nightsNumber * 340)
    return(nightsNumber)

#   Create Variable for the plane ticket and a list of cities
planePrice = 0
cities = ["Port Elizabeth", "Cape Town", "Durban"]

#   Create function for plane costs
def planeCost(planePrice):
    global city
    # City was a local variable making it global will allow it to be used anywhere
    while city != cities:
        if city == "Port Elizabeth":
            planePrice = 1700
            return (planePrice)
        elif city == "Cape Town":
            planePrice = 2800
            return (planePrice)
        elif city == "Durban":
            planePrice = 1200
            return (planePrice)
        else:
            city = input("Please only enter one of these cities that you want to fly to? (Port Elizabeth, Cape Town, Durban)")
       
#   Create function to take in number of days for car rental
def carRental(rentalPrice):
    rentalPrice = float(rentalPrice * 170)
    return(rentalPrice)

#   Create function to calculate the holiday cost
def holidayCost():
    holidayCost = float((hotelCost(nightsNumber)) + (planeCost(planePrice)) + (carRental(rentalPrice)))
    return(f"You will be spending R{holidayCost} for your holiday.")

#   Print out the total cost of the holiday
print(holidayCost())
