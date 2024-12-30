import os
import random
import sys

def game_introduction():
    """
    Introduces the player about the game and its world.
    Opens the prompt to start the game.
    """
    print("You found an ancient book in your late grandma’s basement.")
    print("When you open that book, you find yourself in a fantasy world where people use magic alongside swords and shields, you are no exception.")
    print("The townspeople surround you and proclaim, 'You are the Hero who will save us all!'")
    print("To return to your world, you must conquer the dungeon and fulfill your destiny.")
    start()

def start():
    """
    Gives the player a choice to start the game or not.
    """
    choice = input("Do you want to be the Hero? (y/n) ").lower()
    if choice == "n":
        print("You somehow close the book and walk away. Perhaps another day!")
        quit()
    elif choice == "y":
        print("You accept your destiny as the townspeople cheer wildly!")
        name = input("They ask you your name which is: ")
        print(f"Oh ye mighty Hero {name}, your adventure begins now!")
    else:
        print("Invalid choice. Let's start over")
        start()

def enter_dungeon():
    print("You stand at the entrance of the dungeon as cold wind rushes through you.")
    print("You tighten your grip on your sword and you step inside.")


def confirm_quit():
    confirmation = input("Do you wish to quit your destiny? (y/n) ")
    if confirmation == "n":
        print("You chose not to give up.")
    elif confirmation == "y":
        print("You turn away from your destiny, perhaps another one shall rise..")
    else:
        print("Invalid choice. Let's try again")
        confirm_quit()


def main():
    """
    Runs all game functions
    """
    game_introduction()
    enter_dungeon()

main()