import customtkinter as ctk
from styles import load_icon

class PomodoroApp:
    def __init__(self, root, parent_frame):
        self.root = root
        self.parent_frame = parent_frame

        self.pomodoro_work_time = 25 * 60
        self.pomodoro_break_time = 5 * 60
        
        self.is_working = False
        self.time_left = self.pomodoro_work_time
        
        self.create_widgets()

    def create_widgets(self):
        # Timer section
        timer_frame = ctk.CTkFrame(self.parent_frame)
        timer_frame.pack(fill=ctk.BOTH, expand=True, pady=(40, 20))

        self.timer_label = ctk.CTkLabel(timer_frame, text="25:00", font=("Inter", 48, "bold"))
        self.timer_label.pack(pady=20)

        button_frame = ctk.CTkFrame(timer_frame)
        button_frame.pack(pady=(20, 0))

        start_icon = load_icon("play.png")
        self.start_button = ctk.CTkButton(button_frame, text="Start", image=start_icon, compound="left", command=self.toggle_timer)
        self.start_button.pack(side=ctk.LEFT, padx=10)

        reset_icon = load_icon("reset.png")
        self.reset_button = ctk.CTkButton(button_frame, text="Reset", image=reset_icon, compound="left", command=self.reset_timer)
        self.reset_button.pack(side=ctk.LEFT)

        # Configuration section
        config_frame = ctk.CTkFrame(self.parent_frame)
        config_frame.pack(fill=ctk.BOTH, expand=True, pady=20)

        ctk.CTkLabel(config_frame, text="Work Time (min):").pack(side=ctk.LEFT, padx=(0, 10))
        self.work_time_entry = ctk.CTkEntry(config_frame, width=50)
        self.work_time_entry.insert(0, str(self.pomodoro_work_time // 60))
        self.work_time_entry.pack(side=ctk.LEFT, padx=(0, 20))

        ctk.CTkLabel(config_frame, text="Break Time (min):").pack(side=ctk.LEFT, padx=(0, 10))
        self.break_time_entry = ctk.CTkEntry(config_frame, width=50)
        self.break_time_entry.insert(0, str(self.pomodoro_break_time // 60))
        self.break_time_entry.pack(side=ctk.LEFT)

        save_icon = load_icon("save.png")
        self.save_button = ctk.CTkButton(config_frame, text="Save", image=save_icon, compound="left", command=self.save_config)
        self.save_button.pack(pady=(10, 0))

        # To-Do List section
        todo_frame = ctk.CTkFrame(self.parent_frame)
        todo_frame.pack(fill=ctk.BOTH, expand=True)

        ctk.CTkLabel(todo_frame, text="To-Do List", font=("Inter", 16, "bold")).pack(pady=(0, 10))

        self.todo_listbox = ctk.CTkTextbox(todo_frame, height=200)
        self.todo_listbox.pack(fill=ctk.BOTH, expand=True, padx=(0, 10))

        add_task_frame = ctk.CTkFrame(todo_frame)
        add_task_frame.pack(fill=ctk.X, pady=(10, 0))

        self.add_todo_entry = ctk.CTkEntry(add_task_frame)
        self.add_todo_entry.pack(side=ctk.LEFT, fill=ctk.X, expand=True, padx=(0, 10))
        
        add_icon = load_icon("add.png")
        self.add_todo_button = ctk.CTkButton(add_task_frame, text="Add Task", image=add_icon, compound="left", command=self.add_todo)
        self.add_todo_button.pack(side=ctk.RIGHT)

    def toggle_timer(self):
        if self.is_working:
            self.is_working = False
            self.start_button.configure(text="Start", image=load_icon("play.png"))
        else:
            self.is_working = True
            self.start_button.configure(text="Stop", image=load_icon("stop.png"))
            self.run_timer()

    def run_timer(self):
        if self.is_working:
            if self.time_left > 0:
                minutes, seconds = divmod(self.time_left, 60)
                self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")
                self.time_left -= 1
                self.root.after(1000, self.run_timer)
            else:
                self.toggle_timer()
                if self.time_left == 0:
                    if self.is_working:
                        self.time_left = self.pomodoro_break_time
                        ctk.CTkMessagebox(title="Pomodoro", message="Time for a break!")
                    else:
                        self.time_left = self.pomodoro_work_time
                        ctk.CTkMessagebox(title="Pomodoro", message="Back to work!")
                    
    def reset_timer(self):
        self.is_working = False
        self.time_left = self.pomodoro_work_time
        minutes, seconds = divmod(self.time_left, 60)
        self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")
        self.start_button.configure(text="Start", image=load_icon("play.png"))
    
    def save_config(self):
        try:
            self.pomodoro_work_time = int(self.work_time_entry.get()) * 60
            self.pomodoro_break_time = int(self.break_time_entry.get()) * 60
            self.reset_timer()
            ctk.CTkMessagebox(title="Success", message="Settings saved successfully!")
        except ValueError:
            ctk.CTkMessagebox(title="Error", message="Please enter valid numbers.", icon="cancel")
    
    def add_todo(self):
        task = self.add_todo_entry.get()
        if task:
            self.todo_listbox.insert(ctk.END, f"• {task}\n")
            self.add_todo_entry.delete(0, ctk.END)
