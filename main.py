import tkinter as tk
from datetime import datetime

# End date
a = datetime(2025, 2, 28, 23, 59, 59, 99999)
b = datetime(2021, 3, 1,   0,  0,  0, 0)
tot = (a-b).total_seconds()/60
print(tot)

def update_time():
    if not stop:
        g = datetime.now()
        number = ((a-g).total_seconds())/60
        # Update the time display
        label.config(text = f"{number:,.3f} mins left")
        # Reschedule the function to run again after 100ms
        root.after(100, update_time)

def exit_program():
    global root
    root.destroy()

def configure_window(event):
    # Check if the window is in the normal state (not maximized)
    if root.state() == 'normal':
        # Set the window size to 600x600
        root.geometry('600x600')

# Create the main window
root = tk.Tk()
root.title("TimeRiver")
# Maximize the window
root.state('zoomed')

# Make the window resizable
root.resizable(True, True)

# Set the background color of the window to light red
root.configure(bg='#FFCCCC')

# Bind the configure event to the configure_window function
root.bind('<Configure>', configure_window)

# Variable to indicate whether to stop the timer
stop = False

# Create a label to display the time, with a light red background
label = tk.Label(root, font=("Arial", 30), anchor='center', bg='#FFCCCC')
label.place(relx=0.5, rely=0.5, anchor='center')

# Create a button to stop the timer, with a light red background
button = tk.Button(root, text="Exit", command=exit_program, bg='#FFCCCC')
button.place(relx=0.5, rely=0.6, anchor='center')

# Start the countdown
update_time()

# Start the main event loop
root.mainloop()
