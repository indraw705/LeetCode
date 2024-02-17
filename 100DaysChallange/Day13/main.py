import art
from insData import *
import random


def printBanner():
    print(art.logo)


def compare_followers(team1_player, team2_player):
    return "A" if team1_player['follower_count'] >= team2_player['follower_count'] else "B"


def getNewPlayer():
    randomNum = random.randint(0, 49)
    return data[randomNum]


def is_game_continue():
    is_continue = input(f"You wanna play again ??? press Y to play again !!!!").upper()
    if is_continue == "Y":
        return True
    else:
        return False


def startTheGame():
    score = 0
    is_pass = True
    while is_pass:
        team1_player = getNewPlayer()
        print(f'{team1_player["name"]}\n {team1_player["description"]} \n {team1_player["country"]}')
        print(f"\n{art.vs}\n")
        team2_player = getNewPlayer()
        print(f'{team2_player["name"]}\n {team2_player["description"]} \n {team2_player["country"]}')
        choice = (input("what you think ??? who has more followers A or B ??? \n ")).upper()
        ans = compare_followers(team1_player, team2_player)
        if choice == ans:
            score += 1
        else:
            is_pass = False
            print(f"ThankYou your Score is : {score}")
            break


printBanner()
startTheGame()
while is_game_continue():
    startTheGame()

print("Thankyou...")
