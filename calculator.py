import tkinter as tk
import math

def button_click(event):
    """Handle button click event."""
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "sin":
        try:
            result = math.sin(math.radians(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "cos":
        try:
            result = math.cos(math.radians(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "tan":
        try:
            result = math.tan(math.radians(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

def clear_entry():
    """Clear the entry widget."""
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")

# Create an entry widget for displaying the result
entry = tk.Entry(window,bg='LightGreen' ,font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Create buttons for numbers, operators, and functions
buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "sin",
    "1", "2", "3", "-", "cos",
    "0", ".", "=", "+", "tan"
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(window, text=button,bg='LightBlue', font=("Arial", 15), width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", button_click)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Create a clear button
clear_btn = tk.Button(window, text="Clear",bg='LightBlue', font=("Arial", 15), width=5, height=2, command=clear_entry)
clear_btn.grid(row=row, column=col, padx=5, pady=5)

# Start the main event loop
window.mainloop()