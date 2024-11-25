# PC Scheduler

A Python script with a GUI to schedule shutdown, restart, or sleep commands for Windows.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/dev-arhaan/PC-Scheduler.git
   cd PC-Scheduler
   python schedule_shutdown.py
 
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
