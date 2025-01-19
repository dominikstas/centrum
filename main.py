import tkinter as tk
from tkinter import ttk
from pomodoro_timer import PomodoroApp
from meditation_timer import MeditationApp
from styles import set_custom_style, create_rounded_button

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Productivity Tools")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")
        
        set_custom_style()
        self.create_widgets()
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        title = ttk.Label(main_frame, text="Choose Your Tool", style="Timer.TLabel")
        title.grid(row=0, column=0, pady=(0, 40))
        
        pomodoro_btn = create_rounded_button(main_frame, "Pomodoro Timer", self.open_pomodoro)
        pomodoro_btn.grid(row=1, column=0, pady=10)
        
        meditation_btn = create_rounded_button(main_frame, "Meditation Timer", self.open_meditation)
        meditation_btn.grid(row=2, column=0, pady=10)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
    
    def open_pomodoro(self):
        pomodoro_window = tk.Toplevel(self.root)
        PomodoroApp(pomodoro_window)
    
    def open_meditation(self):
        meditation_window = tk.Toplevel(self.root)
        MeditationApp(meditation_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()