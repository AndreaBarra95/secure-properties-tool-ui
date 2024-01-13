import tkinter as tk
from crypto_operations import *

def create_ui(root, encrypt_callback, decrypt_callback):
    # Widget frames
    input_frame = tk.Frame(root)
    input_frame.pack(padx=120, pady=50)

    # Key's Label and Entry
    key_label = tk.Label(input_frame, text="Key:")
    key_label.grid(row=0, column=0, sticky="w")
    key_entry = tk.Entry(input_frame)
    key_entry.grid(row=0, column=1)

    # Property's Label and Entry
    password_label = tk.Label(input_frame, text="Property:")
    password_label.grid(row=1, column=0, sticky="w")
    password_entry = tk.Entry(input_frame)
    password_entry.grid(row=1, column=1)

    # Encrypted Property Label
    encrypted_label = tk.Label(input_frame, text="Encrypted Property:")
    encrypted_label.grid(row=2, column=0, sticky="w")
    encrypted_password_label = tk.Label(input_frame, text="", wraplength=200)
    encrypted_password_label.grid(row=2, column=1)

    # Decrypted Property Label
    decrypted_label = tk.Label(input_frame, text="Decrypted Property:")
    decrypted_label.grid(row=3, column=0, sticky="w")
    decrypted_password_label = tk.Label(input_frame, text="", wraplength=200)
    decrypted_password_label.grid(row=3, column=1)

    # Buttons to execute encrypt and decrypt actions
    encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_data)
    encrypt_button.pack(pady=5)
    decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_data)
    decrypt_button.pack(pady=5)

    # Button to copy encrypted property
    copy_encrypted_button = tk.Button(input_frame, text="copy", command=copy_encrypted)
    copy_encrypted_button.grid(row=2, column=2, padx=5)

    # Button to copy decrypted property
    copy_decrypted_button = tk.Button(input_frame, text="copy", command=copy_decrypted)
    copy_decrypted_button.grid(row=3, column=2, padx=5)