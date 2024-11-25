import os
import tkinter as tk
from tkinter import messagebox

def schedule_shutdown():
    try:
        minutes = int(entry_minutes.get())
        seconds = minutes * 60
        os.system(f"shutdown /s /t {seconds}")
        messagebox.showinfo("Shutdown Scheduled", f"Your PC will shut down in {minutes} minute(s).")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

def cancel_shutdown():
    os.system("shutdown /a")
    messagebox.showinfo("Shutdown Canceled", "Scheduled shutdown has been canceled.")

def restart_pc():
    try:
        minutes = int(entry_minutes.get())
        seconds = minutes * 60
        os.system(f"shutdown /r /t {seconds}")
        messagebox.showinfo("Restart Scheduled", f"Your PC will restart in {minutes} minute(s).")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

def sleep_pc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    messagebox.showinfo("Sleep Mode", "Your PC is now in sleep mode.")

# Create the main application window
root = tk.Tk()
root.title("PC Power Scheduler")

# Create a label for the minutes input
label_minutes = tk.Label(root, text="Enter minutes for the action:")
label_minutes.pack(pady=10)

# Create an entry widget for minutes input
entry_minutes = tk.Entry(root, width=20)
entry_minutes.pack(pady=5)

# Create buttons for each action
button_schedule_shutdown = tk.Button(root, text="Schedule Shutdown", command=schedule_shutdown)
button_schedule_shutdown.pack(pady=5)

button_restart = tk.Button(root, text="Schedule Restart", command=restart_pc)
button_restart.pack(pady=5)

button_sleep = tk.Button(root, text="Put to Sleep", command=sleep_pc)
button_sleep.pack(pady=5)

button_cancel = tk.Button(root, text="Cancel Shutdown/Restart", command=cancel_shutdown, bg="red", fg="white")
button_cancel.pack(pady=10)

# Run the application
root.mainloop()
