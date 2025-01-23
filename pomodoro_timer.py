import tkinter as tk
from tkinter import ttk, messagebox
from styles import set_custom_style, create_rounded_button

class PomodoroApp:
    def __init__(self, root, parent_frame):
        self.root = root
        self.parent_frame = parent_frame

        set_custom_style()

        self.pomodoro_work_time = 25 * 60
        self.pomodoro_break_time = 5 * 60
        
        self.is_working = False
        self.time_left = self.pomodoro_work_time
        
        self.create_widgets()

    def create_widgets(self):
        self.parent_frame.columnconfigure(0, weight=1)
        
        # Timer section
        timer_frame = ttk.Frame(self.parent_frame, style="TFrame")
        timer_frame.grid(row=1, column=0, sticky="ew", pady=(40, 20))
        timer_frame.columnconfigure(0, weight=1)

        self.timer_label = ttk.Label(timer_frame, text="25:00", style="Timer.TLabel", anchor="center")
        self.timer_label.grid(row=0, column=0, sticky="nsew")

        button_frame = ttk.Frame(timer_frame, style="TFrame")
        button_frame.grid(row=1, column=0, pady=(20, 0))
        
        button_frame.columnconfigure((0, 1), weight=1)

        self.start_button = create_rounded_button(button_frame, "Start", self.toggle_timer)
        self.start_button.grid(row=0, column=0, padx=10)

        self.reset_button = create_rounded_button(button_frame, "Reset", self.reset_timer)
        self.reset_button.grid(row=0, column=1)

        # Configuration section
        config_frame = ttk.Frame(self.parent_frame, style="TFrame")
        config_frame.grid(row=2, column=0, sticky="ew", pady=20)
        config_frame.columnconfigure((0, 2), weight=1)

        ttk.Label(config_frame, text="Work Time (min):", style="Config.TLabel").grid(row=0, column=0, sticky="w")
        self.work_time_entry = ttk.Entry(config_frame, width=5, style="Config.TEntry")
        self.work_time_entry.insert(0, str(self.pomodoro_work_time // 60))
        self.work_time_entry.grid(row=0, column=1, padx=(0, 20))

        ttk.Label(config_frame, text="Break Time (min):", style="Config.TLabel").grid(row=0, column=2, sticky="w")
        self.break_time_entry = ttk.Entry(config_frame, width=5, style="Config.TEntry")
        self.break_time_entry.insert(0, str(self.pomodoro_break_time // 60))
        self.break_time_entry.grid(row=0, column=3)

        self.save_button = create_rounded_button(config_frame, "Save", self.save_config)
        self.save_button.grid(row=1, column=0, columnspan=4, pady=(10, 0))

        # To-Do List section
        todo_frame = ttk.Frame(self.parent_frame, style="TFrame")
        todo_frame.grid(row=3, column=0, sticky="nsew")
        todo_frame.columnconfigure(0, weight=1)

        ttk.Label(todo_frame, text="To-Do List", font=("Helvetica", 16, "bold"), style="TLabel").grid(row=0, column=0, pady=(0, 10))

        list_frame = ttk.Frame(todo_frame, style="TFrame")
        list_frame.grid(row=1, column=0, sticky="nsew")
        list_frame.columnconfigure(0, weight=1)

        self.todo_listbox = tk.Listbox(list_frame, height=10, selectmode=tk.SINGLE, 
                                       font=("Helvetica", 12), bg="white", fg="#333333",
                                       selectbackground="#4CAF50", selectforeground="white",
                                       highlightthickness=0, bd=0)
        self.todo_listbox.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.todo_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.todo_listbox.config(yscrollcommand=scrollbar.set)

        add_task_frame = ttk.Frame(todo_frame, style="TFrame")
        add_task_frame.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        add_task_frame.columnconfigure(0, weight=1)

        self.add_todo_entry = ttk.Entry(add_task_frame, style="Todo.TEntry")
        self.add_todo_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        
        self.add_todo_button = create_rounded_button(add_task_frame, "Add Task", self.add_todo)
        self.add_todo_button.grid(row=0, column=1)

    def toggle_timer(self):
        if self.is_working:
            self.is_working = False
            self.start_button.config(text="Start")
        else:
            self.is_working = True
            self.start_button.config(text="Stop")
            self.run_timer()

    def run_timer(self):
        if self.is_working:
            if self.time_left > 0:
                minutes, seconds = divmod(self.time_left, 60)
                self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
                self.time_left -= 1
                self.root.after(1000, self.run_timer)
            else:
                self.toggle_timer()
                if self.time_left == 0:
                    if self.is_working:
                        self.time_left = self.pomodoro_break_time
                        messagebox.showinfo("Pomodoro", "Time for a break!")
                    else:
                        self.time_left = self.pomodoro_work_time
                        messagebox.showinfo("Pomodoro", "Back to work!")
                    
    def reset_timer(self):
        self.is_working = False
        self.time_left = self.pomodoro_work_time
        minutes, seconds = divmod(self.time_left, 60)
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        self.start_button.config(text="Start")
    
    def save_config(self):
        try:
            self.pomodoro_work_time = int(self.work_time_entry.get()) * 60
            self.pomodoro_break_time = int(self.break_time_entry.get()) * 60
            self.reset_timer()
            messagebox.showinfo("Success", "Settings saved successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
    
    def add_todo(self):
        task = self.add_todo_entry.get()
        if task:
            self.todo_listbox.insert(tk.END, task)
            self.add_todo_entry.delete(0, tk.END)