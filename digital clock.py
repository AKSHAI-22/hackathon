import tkinter as tk
from time import strftime
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)
label = tk.Label(root, font=("Helvetica", 50), fg="cyan", bg="black")
label.pack(expand=True)
def update_time():
    current_time = strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, update_time)
update_time()
root.mainloop()
