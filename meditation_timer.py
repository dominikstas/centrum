import tkinter as tk
from tkinter import ttk, messagebox
from styles import set_custom_style, create_rounded_button
from pygame import mixer

class MeditationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meditation Stopwatch")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        set_custom_style()
        
        self.elapsed_time = 0
        self.is_meditating = False
        
        # Initialize sound
        mixer.init()
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=1)
        
        # Timer display
        self.timer_label = ttk.Label(main_frame, text="00:00:00", style="Timer.TLabel")
        self.timer_label.grid(row=0, column=0, pady=(0, 20))
        
        # Controls frame
        controls_frame = ttk.Frame(main_frame)
        controls_frame.grid(row=1, column=0, pady=20)
        
        self.start_button = create_rounded_button(controls_frame, "Start", self.toggle_timer)
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.reset_button = create_rounded_button(controls_frame, "Reset", self.reset_timer)
        self.reset_button.grid(row=0, column=1)
        
        # Last session frame
        self.last_session_frame = ttk.Frame(main_frame)
        self.last_session_frame.grid(row=2, column=0, pady=20)
        
        self.last_session_label = ttk.Label(
            self.last_session_frame, 
            text="Last session duration: 00:00:00",
            style="Config.TLabel"
        )
        self.last_session_label.grid(row=0, column=0)
        
        # Configure grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def toggle_timer(self):
        if self.is_meditating:
            self.is_meditating = False
            self.start_button.config(text="Start")
            # Save last session duration
            self.last_session_label.config(
                text=f"Last session duration: {self.format_time(self.elapsed_time)}"
            )
            self.play_ending_sound()
        else:
            self.is_meditating = True
            self.start_button.config(text="Stop")
            self.run_timer()
    
    def run_timer(self):
        if self.is_meditating:
            self.elapsed_time += 1
            self.timer_label.config(text=self.format_time(self.elapsed_time))
            self.root.after(1000, self.run_timer)
    
    def reset_timer(self):
        self.is_meditating = False
        self.elapsed_time = 0
        self.timer_label.config(text="00:00:00")
        self.start_button.config(text="Start")
    
    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def play_ending_sound(self):
        # You can add a gentle bell sound here
        # For now, we'll just use the system bell
        self.root.bell()