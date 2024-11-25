import os
import platform
import tkinter as tk
from tkinter import messagebox

def get_current_os():
    return platform.system()

def schedule_shutdown():
    try:
        minutes = int(entry_minutes.get())
        seconds = minutes * 60
        current_os = get_current_os()

        if current_os == "Windows":
            os.system(f"shutdown /s /t {seconds}")
        elif current_os in ("Linux", "Darwin"):  # Darwin is macOS
            os.system(f"shutdown -h +{minutes}")
        else:
            messagebox.showerror("Unsupported OS", "Shutdown is not supported on this OS.")
            return
        
        messagebox.showinfo("Shutdown Scheduled", f"Your PC will shut down in {minutes} minute(s).")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

def cancel_shutdown():
    current_os = get_current_os()

    if current_os == "Windows":
        os.system("shutdown /a")
    elif current_os in ("Linux", "Darwin"):
        os.system("shutdown -c")
    else:
        messagebox.showerror("Unsupported OS", "Cancel shutdown is not supported on this OS.")
        return

    messagebox.showinfo("Shutdown Canceled", "Scheduled shutdown has been canceled.")

def restart_pc():
    try:
        minutes = int(entry_minutes.get())
        seconds = minutes * 60
        current_os = get_current_os()

        if current_os == "Windows":
            os.system(f"shutdown /r /t {seconds}")
        elif current_os in ("Linux", "Darwin"):
            os.system(f"shutdown -r +{minutes}")
        else:
            messagebox.showerror("Unsupported OS", "Restart is not supported on this OS.")
            return
        
        messagebox.showinfo("Restart Scheduled", f"Your PC will restart in {minutes} minute(s).")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

def sleep_pc():
    current_os = get_current_os()

    if current_os == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif current_os == "Darwin":  # macOS
        os.system("pmset sleepnow")
    elif current_os == "Linux":
        os.system("systemctl suspend")
    else:
        messagebox.showerror("Unsupported OS", "Sleep is not supported on this OS.")
        return

    messagebox.showinfo("Sleep Mode", "Your PC is now in sleep mode.")

# Create the main application window
root = tk.Tk()
root.title("Cross-Platform PC Power Scheduler")

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
