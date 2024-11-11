'''CALCULATOR
TASK 2
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result'''
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(root, text="Clear", width=23, command=self.clear).grid(row=row_val, column=0, columnspan=4)

    def click_button(self, button):
        if button == '=':
            try:
                self.expression = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.expression)
            except Exception as e:
                self.expression = "Error"
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.expression)
        else:
            self.expression += str(button)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()



