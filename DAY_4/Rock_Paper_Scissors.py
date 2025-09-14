rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
pattern = [rock,paper,scissors]

import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)


if user_choice >=0 and user_choice<3:
    print(f"Your Choice: {user_choice}")
    print(pattern[user_choice])
    print("Computer Chose: ")
    print(pattern[computer_choice])

if user_choice>=3 or user_choice<0:
    print("You Entered a wrong number. YOU LOST!!")
elif user_choice == computer_choice:
    print("It's a Draw !!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice== 0):
    print("You WON !!")
else:
    print("You LOST !!")

