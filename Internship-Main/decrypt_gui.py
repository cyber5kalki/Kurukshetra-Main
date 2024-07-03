import os
import customtkinter as ctk
from tkinter import filedialog
from decrypt import decrypt_file
from threading import Thread
import time
import queue
import tkinter  # Add this import

def select_files():
    encrypted_filename = filedialog.askopenfilename()
    fek_filename = filedialog.askopenfilename()
    if encrypted_filename and fek_filename:
        encrypted_file_entry.delete(0, 'end')
        encrypted_file_entry.insert('end', encrypted_filename)
        fek_file_entry.delete(0, 'end')
        fek_file_entry.insert('end', fek_filename)

def show_custom_message(title, message, on_close=None):
    message_dialog = ctk.CTk()
    message_dialog.title(title)
    message_dialog.geometry("700x100")

    def close_dialog():
        message_dialog.destroy()
        if on_close:
            on_close()

    ctk.CTkLabel(message_dialog, text=message).pack(padx=20, pady=10)
    ctk.CTkButton(message_dialog, text="OK", command=close_dialog).pack(pady=10)
    message_dialog.mainloop()

def update_status(message):
    try:
        if root.winfo_exists() and status_label.winfo_exists():
            status_label.configure(text=message)
            root.update()
    except tkinter.TclError as e:
        print(f"Error updating status: {e}")

def update_progress(value):
    try:
        if root.winfo_exists() and progress_bar.winfo_exists():
            progress_bar.set(value)
            root.update()
    except tkinter.TclError as e:
        print(f"Error updating progress: {e}")

def decrypt():
    encrypted_file_path = encrypted_file_entry.get()
    fek_file_path = fek_file_entry.get()
    passphrase = passphrase_entry.get()

    if not encrypted_file_path or not fek_file_path or not passphrase:
        show_custom_message("Error", "Please select both files and enter a passphrase.")
        return

    def perform_decryption():
        update_queue.put(("progress", 1.0))  # Start with the progress bar full
        update_queue.put(("status", f"Reading the encrypted file '{os.path.basename(encrypted_file_path)}'..."))
        time.sleep(1)  # Simulate delay
        update_queue.put(("progress", 0.75))  # Update the progress bar

        try:
            update_queue.put(("status", f"Decrypting data from '{os.path.basename(encrypted_file_path)}'..."))
            result = decrypt_file(encrypted_file_path, fek_file_path, passphrase)
            time.sleep(1)  # Simulate delay
            update_queue.put(("progress", 0.5))  # Update the progress bar

            if result == "Incorrect password":
                update_queue.put(("message", ("Error", "Wrong passphrase. Decryption failed.")))
                update_queue.put(("progress", 1.0))  # Reset the progress bar
                return

            update_queue.put(("status", f"Saving decrypted file '{os.path.basename(encrypted_file_path)}'..."))
            time.sleep(1)  # Simulate delay
            update_queue.put(("progress", 0.25))  # Update the progress bar

            update_queue.put(("progress", 0.0))  # Decryption complete
            update_queue.put(("message", ("Success", result, root.destroy)))
        except Exception as e:
            update_queue.put(("message", ("Error", f"Decryption failed: {str(e)}")))
            update_queue.put(("progress", 1.0))  # Reset the progress bar
        finally:
            update_queue.put(("status", ""))

    Thread(target=perform_decryption).start()

def process_queue():
    if not app_running:
        return
    try:
        while True:
            task = update_queue.get_nowait()
            if task[0] == "progress":
                update_progress(task[1])
            elif task[0] == "status":
                update_status(task[1])
            elif task[0] == "message":
                show_custom_message(*task[1])
            update_queue.task_done()
    except queue.Empty:
        pass
    root.after(100, process_queue)

def on_closing():
    global app_running
    app_running = False
    root.destroy()

# Create GUI window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Decryption")
root.geometry("700x300")
root.protocol("WM_DELETE_WINDOW", on_closing)

# Labels and Entries
ctk.CTkLabel(root, text="Encrypted File:").grid(row=0, column=0, padx=10, pady=10)
encrypted_file_entry = ctk.CTkEntry(root, width=400)
encrypted_file_entry.grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(root, text="Browse", command=select_files).grid(row=0, column=2, padx=10, pady=10)

ctk.CTkLabel(root, text="FEK File:").grid(row=1, column=0, padx=10, pady=10)
fek_file_entry = ctk.CTkEntry(root, width=400)
fek_file_entry.grid(row=1, column=1, padx=10, pady=10)
ctk.CTkButton(root, text="Browse", command=select_files).grid(row=1, column=2, padx=10, pady=10)

ctk.CTkLabel(root, text="Passphrase:").grid(row=2, column=0, padx=10, pady=10)
passphrase_entry = ctk.CTkEntry(root, show="*", width=400)
passphrase_entry.grid(row=2, column=1, padx=10, pady=10)

status_label = ctk.CTkLabel(root, text="")
status_label.grid(row=3, column=1, pady=10)

progress_bar = ctk.CTkProgressBar(root, width=400, height=20)
progress_bar.grid(row=4, column=1, pady=10)
progress_bar.set(1)

ctk.CTkButton(root, text="Decrypt", command=decrypt).grid(row=5, column=1, pady=20)

# Queue for GUI updates
update_queue = queue.Queue()
app_running = True
root.after(100, process_queue)

root.mainloop()