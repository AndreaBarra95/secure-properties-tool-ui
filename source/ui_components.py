import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from crypto_operations import decrypt_data, encrypt_data, copy_decrypted, copy_encrypted, reset_copy_button

def create_ui(root, encrypt_callback, decrypt_callback):
    # Bootstrap style
    style = Style(theme='flatly')

    # Widget frames
    input_frame = ttk.Frame(root, padding='20 10 20 10')
    input_frame.grid(row=0, column=0, sticky='nsew')

    # Widget style
    ttk.Label(input_frame, text="Key:").grid(row=0, column=0, sticky='w')
    key_entry = ttk.Entry(input_frame)
    key_entry.grid(row=0, column=1)

    ttk.Label(input_frame, text="Property:").grid(row=1, column=0, sticky='w')
    password_entry = ttk.Entry(input_frame)
    password_entry.grid(row=1, column=1)

    ttk.Label(input_frame, text="Encrypted Property:").grid(row=2, column=0, sticky='w')
    encrypted_password_label = ttk.Label(input_frame, wraplength=200)
    encrypted_password_label.grid(row=2, column=1)

    ttk.Label(input_frame, text="Decrypted Property:").grid(row=3, column=0, sticky='w')
    decrypted_password_label = ttk.Label(input_frame, wraplength=200)
    decrypted_password_label.grid(row=3, column=1)

    # Dropdown menu for the algorithm choice
    algorithm_choice = tk.StringVar()
    algorithm_choice.set("Blowfish CBC")  # Opzione predefinita
    algorithm_menu = ttk.Combobox(root, textvariable=algorithm_choice, values=["Blowfish CBC", "AES CBC"])
    algorithm_menu.grid(row=1, column=0, sticky='nsew')

    # Buttons
    encrypt_button = ttk.Button(root, text="Encrypt", command=lambda: encrypt_data(key_entry, password_entry, encrypted_password_label, algorithm_choice.get()))
    encrypt_button.grid(row=2, column=0, pady=5)

    decrypt_button = ttk.Button(root, text="Decrypt", command=lambda: decrypt_data(key_entry, encrypted_password_label, decrypted_password_label, algorithm_choice.get()))
    decrypt_button.grid(row=3, column=0, pady=5)

    copy_encrypted_button = ttk.Button(input_frame, text="Copy", command=lambda: copy_encrypted(encrypted_password_label, copy_encrypted_button, root))
    copy_encrypted_button.grid(row=2, column=2, padx=5)

    copy_decrypted_button = ttk.Button(input_frame, text="Copy", command=lambda: copy_decrypted(decrypted_password_label, copy_decrypted_button, root))
    copy_decrypted_button.grid(row=3, column=2, padx=5)

    # Responsiveness configuration
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    input_frame.grid_rowconfigure(0, weight=1)
    input_frame.grid_columnconfigure(1, weight=1)
