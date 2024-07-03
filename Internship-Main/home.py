import customtkinter as ctk
import subprocess
from PIL import Image, ImageSequence
import os
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Get the base directory of the script
base_dir = os.path.dirname(os.path.abspath(__file__))

def open_encryption_decryption_app():
    try:
        # Use relative path example
        script_path = os.path.join(base_dir, 'encryption_decryption_app.py')
        if os.path.exists(script_path):
            logging.debug(f"Starting {script_path}")
            subprocess.Popen([sys.executable, script_path])
            root.destroy()  # Close the current window
        else:
            logging.error(f"File not found: {script_path}")
            error_label.config(text=f"File not found: {script_path}")
    except Exception as e:
        logging.error(f"Failed to open encryption_decryption_app.py: {e}")
        error_label.config(text=f"Failed to open encryption_decryption_app.py: {e}")

def exit_application():
    root.destroy()

# Function to update the GIF frames
def update_gif(label, gif_frames, frame_index):
    frame = gif_frames[frame_index]
    frame_index = (frame_index + 1) % len(gif_frames)
    label.configure(image=frame)
    root.after(50, update_gif, label, gif_frames, frame_index)  # Reduced delay to increase speed

# Create the main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green") 

root = ctk.CTk()
root.title("Kurukshetra")
root.geometry("500x650")  # Set the window size

# Label for welcome message
welcome_label = ctk.CTkLabel(root, text="Welcome to Kurukshetra\n", font=("Helvetica", 27, "bold"))
welcome_label.pack(pady=10)

# Label for the event description
description_label = ctk.CTkLabel(root, text="Protecting User Password Keys at Rest (on the Disk)", font=("Helvetica", 17, "italic"))
description_label.pack(pady=10)

# Load the GIF and create a list of frames with a medium size
gif_path = os.path.join(base_dir,'images', 'kurukshetra.gif')  # Use relative path
try:
    gif_image = Image.open(gif_path)
    new_size = (300, 300)  # Adjust the size to medium
    gif_frames = [ctk.CTkImage(frame.copy().convert("RGBA"), size=new_size) for frame in ImageSequence.Iterator(gif_image)]
except FileNotFoundError:
    logging.error(f"GIF file not found: {gif_path}")
    gif_frames = []  # Ensure gif_frames is defined even if there's an error

# Label to display the GIF without any text
gif_label = ctk.CTkLabel(root, text="")
gif_label.pack(pady=10)

if gif_frames:
    update_gif(gif_label, gif_frames, 0)

# Button to navigate to the encryption/decryption app
navigate_button = ctk.CTkButton(root, text="Encryption/Decryption", command=open_encryption_decryption_app)
navigate_button.pack(pady=10)

# Label to display errors
error_label = ctk.CTkLabel(root, text="", font=("Helvetica", 12, "bold"), text_color="red")
error_label.pack(pady=10)

# Frame to contain the quit button at the bottom
bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(side="bottom", fill="x")

# Center the quit button within the bottom frame
quit_button = ctk.CTkButton(bottom_frame, text="Quit", command=exit_application, fg_color="#e74c3c", hover_color="#c0392b", text_color="#ecf0f1", font=("Helvetica", 15, "bold"))
quit_button.pack(pady=10)

root.mainloop()