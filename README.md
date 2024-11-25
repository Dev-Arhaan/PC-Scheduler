# PC Scheduler

A Python script with a GUI to schedule shutdown, restart, or sleep commands for Windows.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/dev-arhaan/PC-Scheduler.git
   cd PC-Scheduler
   python schedule_shutdown.py

![Screenshot 2024-11-25 165221](https://github.com/user-attachments/assets/448177fa-a037-4b30-b4d4-2499dab7e444)


## Features:

Shutdown Command:
- Schedule the shutdown.

Sleep Command:

- Immediately puts the PC to sleep.
- Uses rundll32.exe powrprof.dll,SetSuspendState.

Restart Command:

- Schedules a PC restart after the input time.

Cancel Command:

- Cancels scheduled shutdown or restart actions.
  
The script is specifically for Windows due to the shutdown and rundll32 commands.

## Prerequisites:
- Python 3.x

## Next Steps:
- Add error logging or a countdown timer in the GUI for better user experience.
- Test compatibility across different versions of Windows.
