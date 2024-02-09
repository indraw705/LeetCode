import os
import random
from time import sleep

banner = '''
 _______   ____ ___  _____      ________ ____ ______________ _________ _________.___ _______    ________ 
 \      \ |    |   \/     \    /  _____/|    |   \_   _____//   _____//   _____/|   |\      \  /  _____/ 
 /   |   \|    |   /  \ /  \  /   \  ___|    |   /|    __)_ \_____  \ \_____  \ |   |/   |   \/   \  ___ 
/    |    \    |  /    Y    \ \    \_\  \    |  / |        \/        \/        \|   /    |    \    \_\  /\ 
\____|__  /______/\____|__  /  \______  /______/ /_______  /_______  /_______  /|___\____|__  /\______  /
 
'''


def loadingScreen():
    os.system("cls")
    msg = "Loading.."
    for x in range(3):
        msg = msg + "."
        print(msg)
        sleep(1)
        os.system("cls")

    print("%sDone!" % msg)
    print(banner)


def play_game():
    chosen_level = input("\n Choose you Level \n\t Press H for Hard  \n\t Press E for easy \n").upper()
    if chosen_level == 'H':
        attempt = 5
    else:
        attempt = 10
    NUMBER = random.randint(1, 100)
    while attempt:
        guessed_number = int(input("Guess the number \n"))
        if guessed_number == NUMBER:
            print("hurry You got correct ans")
            break
        elif guessed_number > NUMBER:
            attempt -= 1
            print("ummm No!! its too HIGH \n guess again please \n")
            print(f"remaining attempts : {attempt}")
            if attempt==0:
                print(f"Sorry You ran out of attempts & number was {NUMBER}")
        elif guessed_number < NUMBER:
            attempt -= 1
            print("ummm No!! its too Low \n guess again please \n")
            print(f"remaining attempts : {attempt}")
            if attempt==0:
                print(f"Sorry You ran out of attempts & number was {NUMBER}")

    is_continue = input("You wanna play again then press Y !!")
    if is_continue == "Y":
        os.system("cls")
        loadingScreen()
        play_game()


is_game_on = True
loadingScreen()
play_game()
print("Thankyou!!!!!!");
