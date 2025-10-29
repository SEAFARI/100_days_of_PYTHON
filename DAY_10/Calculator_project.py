import art

def add(n1, n2):
    print(f"{n1} + {n2}")
    return n1 + n2

def subtract(n1, n2):
    print(f"{n1} - {n2}")
    return n1 - n2

def divide(n1, n2):
    print(f"{n1} / {n2}")
    return n1/n2

def multiply(n1, n2):
    if n2 == 0:
        print("Division by 0 is not allowed.")
        return
    print(f"{n1} * {n2}")
    return n1 * n2

continue_calc = "n"

while True:
    if continue_calc == "n":
        print("\n"*20)
        print(art.logo)
        first_number = float(input("What is the First Number?: "))
    else:
        first_number = number
    print("+\n-\n*\n/")
    operation = input("Enter an operation to perform.")
    second_number = float(input("What is the second Number?: "))

    if operation == "+":
        number = add(first_number,second_number)
        print(number)
    elif operation == "-":
        number = subtract(first_number, second_number)
        print(number)
    elif operation == "/":
        number = divide(first_number, second_number)
        print(number)
    elif operation == "*":
        number = multiply(first_number, second_number)
        print(number)
    continue_calc = input(f"Type 'y' to continue with {number}, or type 'n' to start a new calculation: ")
