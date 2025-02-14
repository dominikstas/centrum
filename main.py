import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from pomodoro_timer import PomodoroApp
from meditation_timer import MeditationApp
from styles import set_custom_style, create_rounded_button, load_icon

class ProductivityApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Productivity Tools")
        self.geometry("600x800")
        
        set_custom_style()
        
        self.current_frame = None
        self.create_menu()
        
        # Dark mode toggle
        self.dark_mode_var = tk.BooleanVar(value=True)
        self.dark_mode_switch = ctk.CTkSwitch(self, text="Dark Mode", variable=self.dark_mode_var, command=self.toggle_dark_mode)
        self.dark_mode_switch.pack(pady=10, padx=10, anchor="ne")
    
    def create_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ctk.CTkFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title = ctk.CTkLabel(self.current_frame, text="Choose Your Tool", font=("Inter", 32, "bold"))
        title.pack(pady=(0, 40))
        
        pomodoro_icon = load_icon("pomodoro.png")
        pomodoro_btn = ctk.CTkButton(self.current_frame, text="Pomodoro Timer", image=pomodoro_icon, compound="left", command=self.open_pomodoro)
        pomodoro_btn.pack(pady=10)
        
        meditation_icon = load_icon("meditation.png")
        meditation_btn = ctk.CTkButton(self.current_frame, text="Meditation Timer", image=meditation_icon, compound="left", command=self.open_meditation)
        meditation_btn.pack(pady=10)
    
    def open_pomodoro(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ctk.CTkFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        back_icon = load_icon("back.png")
        back_btn = ctk.CTkButton(self.current_frame, text="Back to Menu", image=back_icon, compound="left", command=self.create_menu)
        back_btn.pack(anchor="nw", padx=10, pady=10)
        
        PomodoroApp(self, self.current_frame)
    
    def open_meditation(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ctk.CTkFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        back_icon = load_icon("back.png")
        back_btn = ctk.CTkButton(self.current_frame, text="Back to Menu", image=back_icon, compound="left", command=self.create_menu)
        back_btn.pack(anchor="nw", padx=10, pady=10)
        
        MeditationApp(self, self.current_frame)
    
    def toggle_dark_mode(self):
        new_mode = "dark" if self.dark_mode_var.get() else "light"
        ctk.set_appearance_mode(new_mode)

if __name__ == "__main__":
    app = ProductivityApp()
    app.mainloop()
