import tkinter as tk
from tkinter import ttk

def set_custom_style():
    style = ttk.Style()
    
    # Define color palette
    colors = {
        'bg_dark': '#1a1a1a',        # Main background
        'bg_medium': '#2d2d2d',      # Secondary background
        'accent': '#7289da',         # Primary accent color
        'accent_hover': '#5b6eae',   # Accent hover state
        'text': '#ffffff',           # Primary text
        'text_secondary': '#b3b3b3', # Secondary text
        'disabled': '#404040'        # Disabled state
    }
    
    # Configure base theme
    style.configure(".",
                   background=colors['bg_dark'],
                   foreground=colors['text'],
                   troughcolor=colors['bg_medium'],
                   selectbackground=colors['accent'],
                   selectforeground=colors['text'],
                   fieldbackground=colors['bg_medium'])
    
    # Frame styling
    style.configure("TFrame",
                   background=colors['bg_dark'])
    
    # Label styling
    style.configure("TLabel",
                   background=colors['bg_dark'],
                   foreground=colors['text'],
                   font=("Inter", 11))
    
    # Button styling
    style.configure("TButton",
                   background=colors['accent'],
                   foreground=colors['text'],
                   font=("Inter", 11, "bold"),
                   padding=(20, 10),
                   borderwidth=0,
                   relief="flat")
    
    style.map("TButton",
             background=[('active', colors['accent_hover']),
                        ('disabled', colors['disabled'])],
             foreground=[('disabled', colors['text_secondary'])])
    
    # Timer label specific styling
    style.configure("Timer.TLabel",
                   font=("Inter", 48, "bold"),
                   foreground=colors['text'],
                   background=colors['bg_dark'],
                   padding=20)
    
    # Configuration elements styling
    style.configure("Config.TLabel",
                   padding=(0, 8),
                   font=("Inter", 11))
    
    style.configure("Config.TEntry",
                   padding=8,
                   fieldbackground=colors['bg_medium'],
                   foreground=colors['text'])
    
    # Todo list styling
    style.configure("Todo.TListbox",
                   background=colors['bg_medium'],
                   foreground=colors['text'],
                   font=("Inter", 11),
                   borderwidth=0,
                   highlightthickness=0)
    
    style.configure("Todo.TEntry",
                   font=("Inter", 11),
                   padding=8,
                   fieldbackground=colors['bg_medium'])

def create_rounded_button(parent, text, command):
    button = tk.Button(parent, 
                      text=text, 
                      command=command,
                      bg='#7289da',
                      fg='#ffffff',
                      font=("Inter", 11, "bold"),
                      relief=tk.FLAT,
                      borderwidth=0,
                      padx=20,
                      pady=10,
                      cursor="hand2")  # Changes cursor to hand on hover
    
    button.bind("<Enter>", lambda e: e.widget.config(bg='#5b6eae'))
    button.bind("<Leave>", lambda e: e.widget.config(bg='#7289da'))
    
    return button

# Optional: Configure root window for consistent dark theme
def configure_root_window(root):
    root.configure(bg='#1a1a1a')
    # Set dark theme for all windows/dialogs
    root.option_add('*TCombobox*Listbox*Background', '#2d2d2d')
    root.option_add('*TCombobox*Listbox*Foreground', '#ffffff')