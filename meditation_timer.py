import tkinter as tk
from tkinter import ttk, messagebox
from styles import set_custom_style, create_rounded_button
import time
from pygame import mixer

class MeditationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meditation Timer")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        set_custom_style()
        
        self.meditation_time = 10 * 60  # Default 10 minutes
        self.time_left = self.meditation_time
        self.is_meditating = False
        
        # Initialize sound
        mixer.init()
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=1)
        
        # Timer display
        self.timer_label = ttk.Label(main_frame, text="10:00", style="Timer.TLabel")
        self.timer_label.grid(row=0, column=0, pady=(0, 20))
        
        # Controls frame
        controls_frame = ttk.Frame(main_frame)
        controls_frame.grid(row=1, column=0, pady=20)
        
        self.start_button = create_rounded_button(controls_frame, "Start", self.toggle_timer)
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.reset_button = create_rounded_button(controls_frame, "Reset", self.reset_timer)
        self.reset_button.grid(row=0, column=1)
        
        # Time selection frame
        time_frame = ttk.Frame(main_frame)
        time_frame.grid(row=2, column=0, pady=20)
        
        ttk.Label(time_frame, text="Meditation Time (minutes):", style="Config.TLabel").grid(row=0, column=0, padx=(0, 10))
        
        self.time_entry = ttk.Entry(time_frame, width=5)
        self.time_entry.insert(0, "10")
        self.time_entry.grid(row=0, column=1)
        
        save_button = create_rounded_button(time_frame, "Set Time", self.save_time)
        save_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))
        
        # Configure grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def toggle_timer(self):
        if self.is_meditating:
            self.is_meditating = False
            self.start_button.config(text="Start")
        else:
            self.is_meditating = True
            self.start_button.config(text="Stop")
            self.run_timer()
    
    def run_timer(self):
        if self.is_meditating and self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.time_left -= 1
            self.root.after(1000, self.run_timer)
        elif self.time_left <= 0:
            self.play_ending_sound()
            self.is_meditating = False
            self.start_button.config(text="Start")
            messagebox.showinfo("Meditation", "Meditation session completed!")
            self.reset_timer()
    
    def reset_timer(self):
        self.is_meditating = False
        self.time_left = self.meditation_time
        minutes, seconds = divmod(self.time_left, 60)
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        self.start_button.config(text="Start")
    
    def save_time(self):
        try:
            minutes = int(self.time_entry.get())
            if minutes <= 0:
                raise ValueError
            self.meditation_time = minutes * 60
            self.reset_timer()
            messagebox.showinfo("Success", "Meditation time updated!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of minutes.")
    
    def play_ending_sound(self):
        # You can add a gentle bell sound here
        # For now, we'll just use the system bell
        self.root.bell()
        