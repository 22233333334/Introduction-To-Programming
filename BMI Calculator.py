#   Ask user for their weight
userWeight = int(input("Please enter your weight: "))

#   Ask user for their height
userHeight = float(input("Please enter your height: "))

#   Calculate BMI
userBMI = round(((userWeight) / ((userHeight)*(userHeight))),2)

#   Print out to user their BMI and the score for their BMI
if userBMI >= 30:
    BMI = "obese"
elif userBMI >=25 and userBMI <30:
    BMI = "overweight"
elif userBMI >=18.5 and userBMI <25:
    BMI = "normal"
elif userBMI <18.5:
    BMI = "underweight"
print(f"Your BMI is {userBMI} and you are {BMI}.")
