import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

opt_arr = [Rock, Paper, Scissors]

userinput = int(input(
    "welcome to ROCK PAPER SCISSORS GAME \n \t Press 0 for Rock  \n \t Press 1 for Paper \n \t Press 2 for Scissors\n"))

if userinput > 2:
    print("Its a wrong choice. \n Try Again !!! \n")
else:
    computer_input = random.randint(0, 2)
    print(f"You Choose \n {opt_arr[userinput]} \n Computer Choose \n  {opt_arr[computer_input]}")
    if userinput == computer_input:
        print("It's Draw !!! Try Again")
    elif userinput == 0 and computer_input == 1:
        print("You Loose ! Computer Won")
    elif userinput == 0 and computer_input == 2:
        print("You Won ! Computer Loose")
    elif userinput == 1 and computer_input == 0:
        print("You Won ! Computer Loose")
    elif userinput == 1 and computer_input == 2:
        print("You Loose ! Computer Won")
    elif userinput == 2 and computer_input == 0:
        print("You Loose ! Computer Won")
    elif userinput == 2 and computer_input == 1:
        print("You Won ! Computer Loose")
