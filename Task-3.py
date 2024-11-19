'''
PASSWORD GENERATOR
TASK 3
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the
password.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen.
'''
# password_generator_tkinter.py

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Labels and Entries
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(root, width=20)
        self.length_entry.pack()

        self.uppercase_label = tk.Label(root, text="Include Uppercase Letters?")
        self.uppercase_label.pack()
        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(root, variable=self.uppercase_var)
        self.uppercase_checkbox.pack()

        self.numbers_label = tk.Label(root, text="Include Numbers?")
        self.numbers_label.pack()
        self.numbers_var = tk.IntVar()
        self.numbers_checkbox = tk.Checkbutton(root, variable=self.numbers_var)
        self.numbers_checkbox.pack()

        self.symbols_label = tk.Label(root, text="Include Symbols?")
        self.symbols_label.pack()
        self.symbols_var = tk.IntVar()
        self.symbols_checkbox = tk.Checkbutton(root, variable=self.symbols_var)
        self.symbols_checkbox.pack()

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        # Password Display
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()
        self.password_display = tk.Text(root, height=5, width=40)
        self.password_display.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        uppercase = self.uppercase_var.get()
        numbers = self.numbers_var.get()
        symbols = self.symbols_var.get()

        characters = string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
        if numbers:
            characters += string.digits
        if symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.delete(1.0, tk.END)
        self.password_display.insert(tk.END, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
    
