# subscripting
print("Hello"[0])
print("Hello"[4])
print("Hello"[-1])   ## Prints the last character

## string
print("123"+"345")  ## concatinated

## Integer --> whole numbers
print(123 + 345)


## LARGE INTEGERS --> In general, we separate large numbers with commas to make it more redable. in python, we do that by using _
print(123_345_678)

## FLOATING POINT NUMBER
print(3.1244)

## BOOLEAN
print(True)
print(False)


## Finding data type
print(type("Hello"))
print(type(123))
print(type(123_12.123_12))
print(type(True))

## Type conversion/ casting
print(int("123") + int(456))
# print(int("abc")) --> value error

print("Number of letters in your name: " + str(len(input("Enter your name"))))


print(4 - 3)
print(5 * 3)
print(5 ** 3) ## exponent

## division 
print(type(6 / 3)) ## implicit type casting
print(type(6 // 3))  ## removes all numbers after the decimal ( CAREFUL !)

## BEDMAS rule : Bracket, Exponent, division or multi, addition or subtraction --> for "or" , the left one will be executed first
print(3 * 3 + 3 / 3 - 3)

'''
Flooring a Number
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).

Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.

Assignment Operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

+=

-=

*=

/=

f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.

'''

int(3.738492) # Becomes 3
round(3.738492) # Becomes 4
round(3.14159) # Becomes 3
round(3.14159, 2) # Becomes 3.14, with 2 decimal places


age = 12
print(f"I am {age} years old") # Will output I am 12 years old.