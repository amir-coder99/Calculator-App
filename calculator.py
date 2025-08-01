# Calculator App

import tkinter as tk
from tkinter import messagebox

# Functions for each operation
def add():
    calculate("add")

def subtract():
    calculate("subtract")

def multiply():
    calculate("multiply")

def divide():
    calculate("divide")

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")        

def exit_app():
    root.destroy()

# GUI Window Setup
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x300")
root.resizable(True, True)

# Input fields
tk.Label(root, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Buttons for operations
tk.Button(root, text="Add (+)", width=15, command=add).pack(pady=5)
tk.Button(root, text="Subtract (-)", width=15, command=subtract).pack(pady=5)
tk.Button(root, text="Multiply (*)", width=15, command=multiply).pack(pady=5)
tk.Button(root, text="Divide (/)", width=15, command=divide).pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Clear and Exit button
tk.Button(root, text="Clear", width=10, command=clear_all, bg="orange").pack(pady=5)
tk.Button(root, text="Exit", width=10, command=exit_app, bg="red", fg="white").pack(pady=5)

# Start the GUI event loop
root.mainloop()

