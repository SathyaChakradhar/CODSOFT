import tkinter as tk
from tkinter import messagebox
import random
import string
class PG:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.create_gui()
    def create_gui(self):
        label = tk.Label(self.root, text="Enter the desired password length:")
        label.pack(pady=10)
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack(pady=10)
        g_b = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        g_b.pack(pady=10)
        self.result_label = tk.Label(self.root, text="Generated Password: ")
        self.result_label.pack(pady=10)
    def generate_password(self):
        try:
            plen= int(self.length_entry.get())
            if plen <= 0:
                messagebox.showerror("Error", "Please enter a positive password length.")
                return
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(plen))
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number for password length.")
root = tk.Tk()
app = PG(root)
root.mainloop()