# In this project, you'll build a countdown timer using Python's time module. 
# The user enters a number of seconds, and the program counts down to zero, updating 
# every second in the terminal. This is a great example of loops, formatting output, 
# and working with time-based functions.


import time

# Ask the user for duration in seconds
seconds = int(input("Enter countdown duration in seconds: "))

# Countdown loop
for remaining in range(seconds, 0, -1):
    minutes = remaining // 60
    sec = remaining % 60
    print(f"\r{minutes:02}:{sec:02}", end="")  # Displays as mm:ss
    time.sleep(1)  # Pauses execution for 1 second

print("\nTime's up!")


# import time
# import tkinter as tk

# def countdown_timer(seconds):
#     """Updates the countdown display every second."""
#     for remaining in range(seconds, 0, -1):
#         minutes = remaining // 60
#         sec = remaining % 60
#         timer_label.config(text=f"{minutes:02}:{sec:02}")  # Updates GUI
#         root.update()
#         time.sleep(1)

#     timer_label.config(text="Time's Up!")  # Show message when countdown finishes

# # Ask user for duration in seconds
# seconds = int(input("Enter countdown duration in seconds: "))

# # Set up Tkinter window
# root = tk.Tk()
# root.title("Countdown Timer")
# root.geometry("300x150")

# # Timer label
# timer_label = tk.Label(root, text="00:00", font=("Arial", 40))
# timer_label.pack(pady=20)

# # Start countdown after window opens
# root.after(100, countdown_timer, seconds)
# root.mainloop()
