from tkinter import Label, Tk
import time

# Setting up the application window
window = Tk()
window.title("Digital Clock")
window.geometry("700x500")  # Window size
window.configure(bg="gray")  # Background color
window.resizable(False, False)  # Disable resizing the window

# Setting up the text properties
clock_label = Label(window, font=("Arial", 51, "bold"), bg="gray", fg="white")
clock_label.pack(pady=200)  # Add padding at the top to center the clock

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S")  # Extract current time in hours, minutes, and seconds
    clock_label.config(text=current_time)  # Update the text on the user interface
    clock_label.after(1000, update_time)  # Update the time every second

# Calling the update_time function
update_time()

# Run the application
window.mainloop()
