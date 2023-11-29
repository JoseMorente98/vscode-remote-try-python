#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random


# Declare global variables

player_score = 0
computer_score = 0


def game():
    # count the score of the player and computer
    print("Welcome to the game scissors, rock, paper!")
    print("Please choose one of the following options: scissors, rock, paper")
    player = input()
    computer = random.choice(["scissors", "rock", "paper"])
    print("The computer chose " + computer + ".")

    if player == computer:
        print("It's a tie!")
    elif player == "scissors":
        if computer == "rock":
            print("The computer wins!")
            global computer_score
            computer_score += 1
        else:
            print("You win!")
            global player_score
            player_score += 1
    elif player == "rock":
        if computer == "paper":
            print("The computer wins!")
            computer_score
            computer_score += 1
        else:
            print("You win!")
            player_score
            player_score += 1
    elif player == "paper":
        if computer == "scissors":
            print("The computer wins!")
            computer_score
            computer_score += 1
        else:
            print("You win!")
            player_score
            player_score += 1
    else:
        print("Please enter a valid option.")

# Ask do you want to play again, if input is incorrect ask again
def play_again():
    game()
    print("Do you want to play again? (y/n)")
    answer = input()
    if answer == "y":
        game()
        play_again()
    elif answer == "n":
        print("Thanks for playing!")
        # print the score of the player and computer
        print("The final score is:")
        print("Player: " + str(player_score))
        print("Computer: " + str(computer_score))
    else:
        print("Please enter a valid option.")
        play_again()

# Start the game
play_again()