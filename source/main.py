import tkinter as tk
from ui_components import create_ui
from crypto_operations import encrypt_data, decrypt_data

# UI initialization
root = tk.Tk()
root.title("Secure Properties Tool - MuleSoft")

create_ui(root, encrypt_data, decrypt_data)

# Tool execution
root.mainloop()
