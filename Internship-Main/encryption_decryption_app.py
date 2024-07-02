import customtkinter as ctk
from tkinter import messagebox
import subprocess
from PIL import Image
import os

# Get the base directory of the script
base_dir = os.path.dirname(os.path.abspath(__file__))

def select_option(option):
    if option == "Encryption":
        subprocess.Popen(['python', os.path.join(base_dir, 'encrypt_gui.py')])
    elif option == "Decryption":
        subprocess.Popen(['python', os.path.join(base_dir, 'decrypt_gui.py')])
    root.destroy()  # Close the current window after launching the subprocess

def exit_application():
    root.destroy()

# Create the main window
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("Kurukshetra")
root.geometry("500x650")  # Set the window size

# Label for "Choose the option"
label_top = ctk.CTkLabel(root, text="Choose the option", font=("Helvetica", 27, "bold"))
label_top.pack(side=ctk.TOP, pady=20)

# Load and resize images
icon_size = (50, 50)  # Set the desired icon size for medium logos
encryption_img_path = os.path.join(base_dir, 'images', 'encryption.png')
decryption_img_path = os.path.join(base_dir, 'images', 'decryption.png')

encryption_img = Image.open(encryption_img_path)
encryption_img = encryption_img.resize(icon_size, Image.LANCZOS)
encryption_photo = ctk.CTkImage(encryption_img, size=icon_size)

decryption_img = Image.open(decryption_img_path)
decryption_img = decryption_img.resize(icon_size, Image.LANCZOS)
decryption_photo = ctk.CTkImage(decryption_img, size=icon_size)

# Button for Encryption
button_encryption = ctk.CTkButton(root, text="Encryption", image=encryption_photo, compound=ctk.TOP, command=lambda: select_option("Encryption"))
button_encryption.place(relx=0.3, rely=0.5, anchor=ctk.CENTER)

# Button for Decryption
button_decryption = ctk.CTkButton(root, text="Decryption", image=decryption_photo, compound=ctk.TOP, command=lambda: select_option("Decryption"))
button_decryption.place(relx=0.7, rely=0.5, anchor=ctk.CENTER)

# Frame to contain the quit button at the bottom
bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(side="bottom", fill="x")

# Center the quit button within the bottom frame
quit_button = ctk.CTkButton(bottom_frame, text="Quit", command=exit_application, fg_color="#e74c3c", hover_color="#c0392b", text_color="#ecf0f1", font=("Helvetica", 15, "bold"))
quit_button.pack(pady=10)

root.mainloop()
