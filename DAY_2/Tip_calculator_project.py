## (150 bill + 150 * 12 % (0.12)) -> 168 or (150 * 1.12) , here 1 represents the 150

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_cal = round((bill / people * (1 + (tip/100))),2)

print(f"Each person should pay: ${bill_cal:.2f}")
