
'''
Rock-Paper-Scissors Game
TASK 4
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and
feedback
'''
import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.score_label = tk.Label(root, text="User Score: 0 - Computer Score: 0", font=("Helvetica", 16))
        self.score_label.pack()

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack()

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("Rock"))
        self.rock_button.pack(side=tk.LEFT)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("Paper"))
        self.paper_button.pack(side=tk.LEFT)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_button.pack(side=tk.LEFT)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.score_label['text'] = f"User Score: {self.user_score} - Computer Score: {self.computer_score}"
        self.result_label['text'] = f"You chose {user_choice}, computer chose {computer_choice}. {result}"

root = tk.Tk()
game = RockPaperScissors(root)
root.mainloop()
