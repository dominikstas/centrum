import tkinter as tk
from tkinter import ttk

def set_custom_style():
    style = ttk.Style()
    
    # Configure colors
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabel", background="#f0f0f0", foreground="#333333", font=("Helvetica", 12))
    style.configure("TButton", 
                    background="#4CAF50", 
                    foreground="white", 
                    font=("Helvetica", 12, "bold"),
                    padding=10,
                    width=15)
    style.map("TButton",
              background=[('active', '#45a049'), ('disabled', '#a0a0a0')])
    
    style.configure("Timer.TLabel", 
                    font=("Helvetica", 48, "bold"), 
                    foreground="#333333",
                    background="#f0f0f0",
                    padding=20)
    
    style.configure("Config.TLabel", padding=(0, 5))
    style.configure("Config.TEntry", padding=5)
    
    style.configure("Todo.TListbox", 
                    background="white", 
                    foreground="#333333", 
                    font=("Helvetica", 12),
                    borderwidth=0,
                    highlightthickness=0)
    
    style.configure("Todo.TEntry", 
                    font=("Helvetica", 12),
                    padding=5)

def create_rounded_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, 
                       bg="#4CAF50", fg="white", 
                       font=("Helvetica", 12, "bold"),
                       relief=tk.FLAT, padx=15, pady=10)
    button.bind("<Enter>", lambda e: e.widget.config(bg="#45a049"))
    button.bind("<Leave>", lambda e: e.widget.config(bg="#4CAF50"))
    return button
