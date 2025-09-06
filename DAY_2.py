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


