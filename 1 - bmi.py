# calculate a person's BMI
# author: Ben Janning

# Get the input from the user and convert height and weight to a float.
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

# Input the formula to calculate the BMI of the user.
BMI = weight / (height/100)**2

#formatting the result to 2 decimal places using the round function
round: BMI = round(BMI, 2)

# Print the result using the inputted Data.
print (f"Your BMI is {BMI}")

