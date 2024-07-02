import os
import customtkinter as ctk
from tkinter import filedialog
from encrypt import encrypt_file  # Ensure encrypt_file is properly imported
from threading import Thread
import time
import re

def select_file():
    filename = filedialog.askopenfilename()
    if filename:
        file_entry.delete(0, 'end')
        file_entry.insert('end', filename)

def show_custom_message(title, message, on_close=None):
    message_dialog = ctk.CTk()
    message_dialog.title(title)
    message_dialog.geometry("750x100")

    def close_dialog():
        message_dialog.destroy()
        if on_close:
            on_close()
            root.destroy()  # Close the main window after success

    ctk.CTkLabel(message_dialog, text=message).pack(padx=20, pady=10)
    ctk.CTkButton(message_dialog, text="OK", command=close_dialog).pack(pady=10)
    message_dialog.mainloop()

def validate_passphrase(passphrase):
    if len(passphrase) < 8:
        return False
    if not re.search(r'[A-Z]', passphrase):
        return False
    if not re.search(r'[a-z]', passphrase):
        return False
    if not re.search(r'[0-9]', passphrase):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', passphrase):
        return False
    return True

def perform_encryption(file_path, passphrase):
    progress_bar.set(0)
    status_label.configure(text=f"Reading file '{os.path.basename(file_path)}'...")
    time.sleep(1)  # Simulate delay

    try:
        progress_bar.set(0.3)  # Update progress bar
        status_label.configure(text=f"Encrypting data from '{os.path.basename(file_path)}'...")
        time.sleep(1)  # Simulate delay

        encrypted_file_path = encrypt_file(file_path, passphrase)
        progress_bar.set(0.7)  # Update progress bar
        status_label.configure(text=f"Saving encrypted file '{os.path.basename(encrypted_file_path)}'...")
        time.sleep(1)  # Simulate delay

        progress_bar.set(1.0)  # Update progress bar
        show_custom_message("Success", f'File encrypted successfully: {os.path.basename(encrypted_file_path)}', on_close=root.quit)
    except Exception as e:
        show_custom_message("Error", f"Encryption failed: {str(e)}")
    finally:
        status_label.configure(text="")
        progress_bar.set(0)

def encrypt():
    file_path = file_entry.get()
    passphrase = passphrase_entry.get()
    if not file_path or not passphrase:
        show_custom_message("Error", "Please select a file and enter a passphrase.")
        return

    if not validate_passphrase(passphrase):
        show_custom_message("Error", "Passphrase must be at least 8 characters long\n include at least one symbol, one lowercase letter, one uppercase letter, and one number.")
        return

    Thread(target=perform_encryption, args=(file_path, passphrase)).start()

# Create GUI window
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("Encryption")
root.geometry("700x280")

# Labels and Entries
ctk.CTkLabel(root, text="File to Encrypt:").grid(row=0, column=0, padx=10, pady=10)
file_entry = ctk.CTkEntry(root, width=400)
file_entry.grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

ctk.CTkLabel(root, text="Passphrase:").grid(row=1, column=0, padx=10, pady=10)
passphrase_entry = ctk.CTkEntry(root, show="*", width=400)
passphrase_entry.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkButton(root, text="Encrypt", command=encrypt).grid(row=2, column=1, pady=20)

status_label = ctk.CTkLabel(root, text="", font=("Helvetica", 12))
status_label.grid(row=3, column=1, pady=10)

progress_bar = ctk.CTkProgressBar(root, width=400, height=20)
progress_bar.grid(row=4, column=1, pady=10)
progress_bar.set(0)

root.mainloop()
