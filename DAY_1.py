# DAY 1

print("hello world!")
print("Hello world!\n"+"Hello world!\n"+"Hello world!\n")
## indendation erorr --> spaces like space and tab

print("Hello"+ input("What is your name?"))
print("Hello"+ " "+ input("what is your name?")+ "!") # adding exclamation mark at the end


## use control + / to convert and entire line to a comment

## len function dosent work with integers
username = input("What is your name?")
length = len(username)
print("Length of your name is: "+ str(length))


# Project: 
user_name = input("What is your name? ")
user_city = input("Which city did you grew up in?? ")
user_pet_name = input("What is your pet's name? ")

print("Your brand name is: "+ user_city+ " "+ user_pet_name)