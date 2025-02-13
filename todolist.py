import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("To-Do List")
root.geometry("450x550")
root.configure(bg="#2E3440")

task_list = []

def add_task():
    task_text = task_entry.get()
    task_date = date_entry.get()
    
    if task_text.strip() == "" or task_date.strip() == "":
        messagebox.showwarning("Error", "Tell me the name of the task and the date!")
        return
    
    task_frame = ctk.CTkFrame(task_scroll_frame, corner_radius=10)
    task_frame.pack(pady=5, fill='x', padx=10)
    
    task_label = ctk.CTkLabel(task_frame, text=f"{task_text} - {task_date}", font=("Arial", 14))
    task_label.pack(side='left', padx=5)
    
    done_button = ctk.CTkButton(task_frame, text="✔", width=30, fg_color="gray", command=lambda: mark_done(done_button))
    done_button.pack(side='right', padx=5)
    
    delete_button = ctk.CTkButton(task_frame, text="X", width=30, fg_color="red", command=lambda: delete_task(task_frame))
    delete_button.pack(side='right')
    
    task_list.append(task_frame)

def mark_done(button):
    button.configure(fg_color="green")

def delete_task(task_frame):
    task_frame.destroy()

def toggle_theme():
    current_theme = ctk.get_appearance_mode()
    new_theme = "Light" if current_theme == "Dark" else "Dark"
    ctk.set_appearance_mode(new_theme)

header_label = ctk.CTkLabel(root, text="To Do List", font=("Arial", 20, "bold"))
header_label.pack(pady=10)

task_entry = ctk.CTkEntry(root, placeholder_text="Tell me the task!", width=300)
task_entry.pack(pady=5, padx=10)

date_entry = ctk.CTkEntry(root, placeholder_text="Date (DD-MM-YYYY)", width=300)
date_entry.pack(pady=5, padx=10)

add_button = ctk.CTkButton(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

theme_button = ctk.CTkButton(root, text="Change Theme", command=toggle_theme)
theme_button.pack(pady=5)

task_scroll_frame = ctk.CTkScrollableFrame(root)
task_scroll_frame.pack(pady=10, fill='both', expand=True, padx=10)

root.mainloop()
