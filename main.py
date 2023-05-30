import tkinter as tk
from datetime import datetime
from math import ceil

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
        # Update the hour bar
        update_hour_bar(g.hour + g.minute/60)
        # Reschedule the function to run again after 100ms
        root.after(100, update_time)
        # Update the hour bar
        update_hour_bar(g.hour + g.minute/60)


def exit_program():
    global root
    root.destroy()

def configure_window(event):
    # Check if the window is in the normal state (not maximized)
    if root.state() == 'normal':
        # Set the window size to 600x600
        root.geometry('600x600')
    draw_grid()

def update_hour_bar(hour):
    for i in range(24):
        if i < hour:
            # Past hours are white
            hour_bar.itemconfig(i+1, fill='white')
        elif i == round(hour):
            # The current hour fades from green to white
            fraction = hour - i
            intensity = min(255, max(0, ceil(255 * (1 - fraction))))
            color = f'#00{intensity:02x}00'
            hour_bar.itemconfig(i+1, fill=color)
        else:
            # Future hours are green
            hour_bar.itemconfig(i+1, fill='green')

def draw_grid(event=None):
    grid_canvas.delete('all')  # clear the previous grid
    width = grid_canvas.winfo_width()
    height = grid_canvas.winfo_height()
    for i in range(0, width, 50):  # adjust the step size as per your requirement
        grid_canvas.create_line([(i, 0), (i, height)], fill='#d3d3d3', dash=(2, 5))
    for i in range(0, height, 50):  # adjust the step size as per your requirement
        grid_canvas.create_line([(0, i), (width, i)], fill='#d3d3d3', dash=(2, 5))

def show_home():
    home_frame.pack(fill='both', expand=True)
    stats_frame.pack_forget()
    customize_frame.pack_forget()

def show_stats():
    stats_frame.pack(fill='both', expand=True)
    home_frame.pack_forget()
    customize_frame.pack_forget()

def show_customize():
    customize_frame.pack(fill='both', expand=True)
    home_frame.pack_forget()
    stats_frame.pack_forget()

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

########################################### BUttons #########################################

# Create a frame for the buttons
button_frame = tk.Frame(root, bg='#FFCCCC')
button_frame.pack(fill='x')

# Create Home, Stats, and Customize buttons
button = tk.Button(button_frame, text="Home", command=show_home)
stats_button = tk.Button(button_frame, text="Stats", command=show_stats)
customize_button = tk.Button(button_frame, text="©", command=show_customize)

# Instead of packing the buttons to the side, we'll use grid to place them in the center of the frame.
button.grid(row=0, column=1, sticky='ew')
stats_button.grid(row=0, column=2, sticky='ew')
customize_button.grid(row=0, column=3, sticky='ew')

# Configure the columns to have equal weight
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)


##############################################################################################
#                                           Home Page                                        #
##############################################################################################

# Create a frame for the home page
# Create a frame for the home page
home_frame = tk.Frame(root, bg='#FFCCCC')
grid_canvas = tk.Canvas(home_frame, bg='#FFDCDC')  # Same background color as the root window
grid_canvas.place(x=0, y=0, relwidth=1, relheight=1)
label = tk.Label(home_frame, font=("Arial", 30), anchor='center', bg='#FFCCCC')
label.place(relx=0.5, rely=0.5, anchor='center')

button = tk.Button(home_frame, text="Exit", command=exit_program, bg='#FFCCCC')
button.place(relx=0.5, rely=0.6, anchor='center')

hour_bar = tk.Canvas(home_frame, width=30, height=500, bg='white')
hour_bar.place(relx=0.95, rely=0.5, anchor='center')
for i in range(24):
    hour_bar.create_rectangle(0, i*500/24, 30, (i+1)*500/24 - 1, fill='green', outline='black')


##############################################################################################
#                                           Stat Page                                        #
##############################################################################################

# Create a frame for the stats page
stats_frame = tk.Frame(root, bg='#FFCCCC')
stats_label = tk.Label(stats_frame, text="Stats page", font=("Arial", 30), bg='#FFCCCC')
stats_label.pack()

##############################################################################################
#                                           Customize Page                                   #
##############################################################################################

# Create a frame for the customize page
customize_frame = tk.Frame(root, bg='#FFCCCC')
customize_label = tk.Label(customize_frame, text="Customize page", font=("Arial", 30), bg='#FFCCCC')
customize_label.pack()

# Start the countdown
update_time()

# Draw the grid
draw_grid()

# Show the home page by default
show_home()

# Start the main event loop
root.mainloop()
