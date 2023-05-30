import tkinter as tk
from datetime import datetime

# End date
a = datetime(2025, 2, 28, 23, 59, 59, 99999)

def update_time():
    if not stop:
        g = datetime.now()
        number = (a-g).total_seconds()
        # Update the time display
        label.config(text = f"{number} sec left")
        # Reschedule the function to run again after 100ms
        root.after(100, update_time)

def stop_timer():
    global stop
    stop = True

# Create the main window
root = tk.Tk()

# Variable to indicate whether to stop the timer
stop = False

# Create a label to display the time
label = tk.Label(root, font=("Arial", 30))
label.pack()

# Create a button to stop the timer
button = tk.Button(root, text="Stop", command=stop_timer)
button.pack()

# Start the countdown
update_time()

# Start the main event loop
root.mainloop()
