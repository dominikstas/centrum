import tkinter as tk
from tkinter import messagebox
import time
import threading

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer & To-Do List")

        self.pomodoro_work_time = 25 * 60  # Domyślny czas pracy (25 minut)
        self.pomodoro_break_time = 5 * 60  # Domyślny czas przerwy (5 minut)
        
        self.is_working = False
        self.time_left = self.pomodoro_work_time
        
        self.create_widgets()
    
    def create_widgets(self):
        # Timer label
        self.timer_label = tk.Label(self.root, text="00:00", font=("Helvetica", 48), width=10)
        self.timer_label.pack(pady=20)
        
        # Przyciski sterujące
        self.start_button = tk.Button(self.root, text="Start", command=self.toggle_timer, font=("Helvetica", 14))
        self.start_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer, font=("Helvetica", 14))
        self.reset_button.pack(pady=10)
        
        # Konfiguracja Pomodoro
        self.config_frame = tk.Frame(self.root)
        self.config_frame.pack(pady=20)
        
        self.work_label = tk.Label(self.config_frame, text="Czas pracy (min):")
        self.work_label.grid(row=0, column=0)
        self.work_time_entry = tk.Entry(self.config_frame, width=5)
        self.work_time_entry.insert(0, str(self.pomodoro_work_time // 60))
        self.work_time_entry.grid(row=0, column=1)
        
        self.break_label = tk.Label(self.config_frame, text="Czas przerwy (min):")
        self.break_label.grid(row=1, column=0)
        self.break_time_entry = tk.Entry(self.config_frame, width=5)
        self.break_time_entry.insert(0, str(self.pomodoro_break_time // 60))
        self.break_time_entry.grid(row=1, column=1)
        
        self.save_button = tk.Button(self.config_frame, text="Zapisz", command=self.save_config)
        self.save_button.grid(row=2, columnspan=2, pady=10)
        
        # To-Do List
        self.todo_frame = tk.Frame(self.root)
        self.todo_frame.pack(pady=20)

        self.todo_listbox = tk.Listbox(self.todo_frame, height=10, width=50, selectmode=tk.SINGLE)
        self.todo_listbox.pack(side=tk.LEFT, padx=10)
        
        self.todo_scrollbar = tk.Scrollbar(self.todo_frame, orient=tk.VERTICAL, command=self.todo_listbox.yview)
        self.todo_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.todo_listbox.config(yscrollcommand=self.todo_scrollbar.set)
        
        self.add_todo_entry = tk.Entry(self.root, width=40)
        self.add_todo_entry.pack(pady=10)
        
        self.add_todo_button = tk.Button(self.root, text="Dodaj zadanie", command=self.add_todo, font=("Helvetica", 14))
        self.add_todo_button.pack(pady=10)
    
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
                        messagebox.showinfo("Pomodoro", "Czas na przerwę!")
                    else:
                        self.time_left = self.pomodoro_work_time
                        messagebox.showinfo("Pomodoro", "Wracamy do pracy!")
                    
    def reset_timer(self):
        self.time_left = self.pomodoro_work_time
        self.timer_label.config(text="00:00")
        self.start_button.config(text="Start")
    
    def save_config(self):
        try:
            self.pomodoro_work_time = int(self.work_time_entry.get()) * 60
            self.pomodoro_break_time = int(self.break_time_entry.get()) * 60
        except ValueError:
            messagebox.showerror("Błąd", "Proszę wprowadzić poprawne liczby.")
    
    def add_todo(self):
        task = self.add_todo_entry.get()
        if task:
            self.todo_listbox.insert(tk.END, task)
            self.add_todo_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
