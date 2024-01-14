from Crypto.Cipher import Blowfish, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from ui_components import *
import pyperclip

def encrypt_data(key_entry, password_entry, encrypted_password_label, algorithm):
    key = key_entry.get().encode('utf-8')
    password = password_entry.get().encode('utf-8')

    if algorithm == "Blowfish CBC":
        
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, get_random_bytes(8))
        ciphertext = cipher.encrypt(pad(password, Blowfish.block_size))
        
        encrypted_password_label.config(text=b64encode(cipher.iv + ciphertext).decode('utf-8'))
        encrypted_password = b64encode(cipher.iv + ciphertext).decode('utf-8')
        pyperclip.copy(encrypted_password)

    else:
        cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
        ciphertext = cipher.encrypt(pad(password, AES.block_size))
        encrypted_password_label.config(text=b64encode(cipher.iv + ciphertext).decode('utf-8'))
        encrypted_password = b64encode(cipher.iv + ciphertext).decode('utf-8')
        pyperclip.copy(encrypted_password)


def decrypt_data(key_entry, encrypted_password_label, decrypted_password_label, algorithm):
    key = key_entry.get().encode('utf-8')
    encrypted = encrypted_password_label.cget("text").encode('utf-8')

    if algorithm == "Blowfish CBC":
        ciphertext = b64decode(encrypted)
        iv = ciphertext[:8]
        ciphertext = ciphertext[8:]
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

        decrypted = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
        decrypted_password_label.config(text=decrypted.decode('utf-8'))
        decrypted_password = decrypted.decode('utf-8')
        pyperclip.copy(decrypted_password)
    
    else:
        ciphertext = b64decode(encrypted)
        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        decrypted_password_label.config(text=decrypted.decode('utf-8'))
        decrypted_password = decrypted.decode('utf-8')
        pyperclip.copy(decrypted_password)



def copy_encrypted(encrypted_password_label, copy_encrypted_button, root):
    encrypted_password = encrypted_password_label.cget("text")
    pyperclip.copy(encrypted_password)
    copy_encrypted_button.config(text="Copied!")
    root.after(3000, reset_copy_button, copy_encrypted_button, "Copy", 3000)

def copy_decrypted(decrypted_password_label, copy_decrypted_button, root):
    decrypted_password = decrypted_password_label.cget("text")
    pyperclip.copy(decrypted_password)
    copy_decrypted_button.config(text="Copied!")
    root.after(3000, reset_copy_button, copy_decrypted_button, "Copy", 3000)

#def reset_copy_button(button):
#    button.config(text="Copy" if button == copy_encrypted_button else "Copy")
    
def reset_copy_button(button, new_text, delay_ms):
    button.config(text=new_text)
    button.after(delay_ms, lambda: button.config(text="Copy"))
