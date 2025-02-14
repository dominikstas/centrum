import customtkinter as ctk
from styles import load_icon
from pygame import mixer

class MeditationApp:
    def __init__(self, root, parent_frame):
        self.root = root
        self.parent_frame = parent_frame
        
        self.elapsed_time = 0
        self.is_meditating = False
        
        # Initialize sound
        mixer.init()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Timer display
        self.timer_label = ctk.CTkLabel(self.parent_frame, text="00:00:00", font=("Inter", 48, "bold"))
        self.timer_label.pack(pady=(40, 20))
        
        # Controls frame
        controls_frame = ctk.CTkFrame(self.parent_frame)
        controls_frame.pack(pady=20)
        
        start_icon = load_icon("play.png")
        self.start_button = ctk.CTkButton(controls_frame, text="Start", image=start_icon, compound="left", command=self.toggle_timer)
        self.start_button.pack(side=ctk.LEFT, padx=10)
        
        reset_icon = load_icon("reset.png")
        self.reset_button = ctk.CTkButton(controls_frame, text="Reset", image=reset_icon, compound="left", command=self.reset_timer)
        self.reset_button.pack(side=ctk.LEFT)
        
        # Last session frame
        self.last_session_frame = ctk.CTkFrame(self.parent_frame)
        self.last_session_frame.pack(pady=20)
        
        self.last_session_label = ctk.CTkLabel(
            self.last_session_frame, 
            text="Last session duration: 00:00:00",
            font=("Inter", 14)
        )
        self.last_session_label.pack()
    
    def toggle_timer(self):
        if self.is_meditating:
            self.is_meditating = False
            self.start_button.configure(text="Start", image=load_icon("play.png"))
            # Save last session duration
            self.last_session_label.configure(
                text=f"Last session duration: {self.format_time(self.elapsed_time)}"
            )
            self.play_ending_sound()
        else:
            self.is_meditating = True
            self.start_button.configure(text="Stop", image=load_icon("stop.png"))
            self.run_timer()
    
    def run_timer(self):
        if self.is_meditating:
            self.elapsed_time += 1
            self.timer_label.configure(text=self.format_time(self.elapsed_time))
            self.root.after(1000, self.run_timer)
    
    def reset_timer(self):
        self.is_meditating = False
        self.elapsed_time = 0
        self.timer_label.configure(text="00:00:00")
        self.start_button.configure(text="Start", image=load_icon("play.png"))
    
    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def play_ending_sound(self):
        # You can add a gentle bell sound here
        # For now, we'll just use the system bell
        self.root.bell()
