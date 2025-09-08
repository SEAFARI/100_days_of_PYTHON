## BMI calculator 
height = int(input("Enter your height (in m): "))
weight = int(input("Enter your weight (in kg): "))

# Calculate the bmi using weight and height.
bmi = weight/ (height**2)

print("Your BMI is: ",bmi)
