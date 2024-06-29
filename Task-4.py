# Rock-Paper-Scissors Game

import random

print("Let's play Rock-Paper-Scissors!")

while True:
    user = input("Do you choose rock, paper, or scissors? ").lower()
    while user not in ["rock", "paper", "scissors"]:
        user = input("Invalid input. Please enter rock, paper, or scissors: ").lower()

    computer = random.choice(["rock", "paper", "scissors"])
    print(f"\nComputer chose {computer}.")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid input. Please enter yes or no: ").lower()
    if play_again == "no":
        break

print("Thank you for playing!")