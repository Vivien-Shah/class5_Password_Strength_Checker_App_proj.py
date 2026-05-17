import tkinter as tk

def check_strength(event=None):
    """Calculates password strength based on length and updates the GUI."""
    password = entry.get()
    length = len(password)
    
    if length == 0:
        strength_label.config(text="Strength: None", fg="black")
    elif length <= 5:
        strength_label.config(text="Strength: Weak", fg="red")
    elif 6 <= length <= 8:
        strength_label.config(text="Strength: Medium", fg="yellow")
    elif 8 < length <= 12:
        strength_label.config(text="Strength: Strong", fg="#90EE90")  # Light Green
    else:
        strength_label.config(text="Strength: Very Strong", fg="green")  # Dark Green

# Initialize the main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(padx=20, pady=20)

# Create GUI widgets
instructions = tk.Label(root, text="Enter your password to check strength:", font=("Arial", 12))
instructions.pack(pady=(20, 10))

entry = tk.Entry(root, show="*", font=("Arial", 14), width=25)
entry.pack(pady=10)

# Bind the entry widget so strength updates dynamically as the user types
entry.bind("<KeyRelease>", check_strength)

strength_label = tk.Label(root, text="Strength: None", font=("Arial", 14, "bold"))
strength_label.pack(pady=30)

# Start the application
root.mainloop()

