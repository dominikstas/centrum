import tkinter as tk
from tkinter import ttk
from pomodoro_timer import PomodoroApp
from meditation_timer import MeditationApp
from styles import set_custom_style, create_rounded_button

class ProductivityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Productivity Tools")
        self.root.geometry("500x700")
        self.root.configure(bg="#f0f0f0")
        
        set_custom_style()
        
        self.current_frame = None
        self.create_menu()
    
    def create_menu(self):
        # Clear any existing frame
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root, padding="20")
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        
        title = ttk.Label(self.current_frame, text="Choose Your Tool", style="Timer.TLabel")
        title.grid(row=0, column=0, pady=(0, 40))
        
        pomodoro_btn = create_rounded_button(self.current_frame, "Pomodoro Timer", self.open_pomodoro)
        pomodoro_btn.grid(row=1, column=0, pady=10)
        
        meditation_btn = create_rounded_button(self.current_frame, "Meditation Timer", self.open_meditation)
        meditation_btn.grid(row=2, column=0, pady=10)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.current_frame.columnconfigure(0, weight=1)
    
    def open_pomodoro(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root, padding="20")
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame.columnconfigure(0, weight=1)
        
        # Create back button
        back_btn = create_rounded_button(self.current_frame, "Back to Menu", self.create_menu)
        back_btn.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        
        # Create Pomodoro app within the main window
        PomodoroApp(self.root, self.current_frame)
    
    def open_meditation(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root, padding="20")
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame.columnconfigure(0, weight=1)
        
        # Create back button
        back_btn = create_rounded_button(self.current_frame, "Back to Menu", self.create_menu)
        back_btn.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        
        # Create Meditation app within the main window
        MeditationApp(self.root, self.current_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductivityApp(root)
    root.mainloop()