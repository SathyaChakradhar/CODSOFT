import tkinter as tk
from tkinter import messagebox
import random
class RPS:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.user_score = 0
        self.computer_score = 0
        self.create_gui()
    def get_user_choice(self):
        user_choice = self.user_choice_var.get().lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            messagebox.showerror("Invalid Choice", "Please choose rock, paper, or scissors.")
            return None
        return user_choice
    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"
    def display_result(self, user_choice, computer_choice, result):
        messagebox.showinfo("Game Result", f"You chose {user_choice}. The computer chose {computer_choice}.\n{result}\nScore: You {self.user_score} - {self.computer_score}")
    def play_game(self):
        user_choice = self.get_user_choice()
        if user_choice is not None:
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(user_choice, computer_choice)
            self.display_result(user_choice, computer_choice, result)
    def create_gui(self):
        label = tk.Label(self.root,text="Choose rock, paper, or scissors:")
        label.pack(pady=50)
        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")
        choices = ["rock", "paper", "scissors"]
        user_choice_menu = tk.OptionMenu(self.root, self.user_choice_var, *choices)
        user_choice_menu.pack(pady=10)
        play_button = tk.Button(self.root, text="Play", command=self.play_game)
        play_button.pack(pady=30)
root = tk.Tk()
game = RPS(root)
root.mainloop()