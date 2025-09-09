## conditional statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("You can't ride the rollercoaster")
    
    
## Modulo operator --> gives remainder

print(10 % 3) ## remainder = 1

## Check if number is even or odd
user_input = int(input("enter a number"))
if user_input % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
    
    
## NESTED IF and elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age >= 18:   ## nested if
        print("You pay $12")
    elif age >=12 and age < 18:  ## elif
        print("You pay $7")
    else:
        print("You pay $5")
else:
    print("Sorry you have to grow taller before you can ride.")


## BMI calculator with interpretations
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi>=18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")


## Multiple IF

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:       ## first if
        bill = 5
        print("The ticket price is $5.")
    elif age <= 18:
        bill = 7
        print("The ticket price is $7.")
    else:
        bill = 12
        print("The ticket price is $12.")

    wants_photo = input("Do you want a photo?? Type Y for yes and N for no")
    if wants_photo == "Y":    ## Second if, Multiple IF statements implemented here for the same indendation level
        ## Add three dollas to the bill
        bill += 3
    print(f"Your total bill is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
