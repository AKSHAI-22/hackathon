import tkinter as tk
from tkinter import messagebox
from datetime import datetime
def calculate_age():
    try:
        dob = entry_dob.get()
        dob_date = datetime.strptime(dob, "%d-%m-%Y")
        today = datetime.today()
        age = today.year - dob_date.year
        if (today.month, today.day) < (dob_date.month, dob_date.day):
            age -= 1
        label_result.config(text=f"Your Age: {age} years")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date in the format dd-mm-yyyy")
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")
label_prompt = tk.Label(root, text="Enter your Date of Birth (dd-mm-yyyy):", font=("Arial", 14))
label_prompt.pack(pady=20)

entry_dob = tk.Entry(root, font=("Arial", 14))
entry_dob.pack(pady=10)

button_calculate = tk.Button(root, text="Calculate Age", font=("Arial", 14), command=calculate_age)
button_calculate.pack(pady=20)

label_result = tk.Label(root, text="Your Age: ", font=("Arial", 16))
label_result.pack(pady=10)
root.mainloop()
