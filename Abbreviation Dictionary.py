#   Create an abbreviation dictionary
abbreviations = {"AB" : "Application Bulletin",
                 "ADMD" : "Administrative Management Domain",
                 "ALS" : "Application Layer Structure",
                 "BCF" : "Bridge Control Facility"}

#  Add 2 more abbreviations with meanings to dictionary
abbreviations["BCP"] = "Basic Control Program"
abbreviations["BIGWU"] = "Banking Industrial and General Workers Union"

#   Ask user to enter abbreviation to find out its meaning
userInput = input("Please enter an abbreviation that you would like to know? ")

#   Check  user input against the dictionary to either get its meaning or print "not found"
if userInput in abbreviations:
    print(abbreviations[userInput])
else:
    print("Abbreviation not found")
