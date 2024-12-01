import tkinter as tk
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

def on_encrypt():
    password = password_entry.get()
    encrypted = encrypt_password(password, key)
    encrypted_label.config(text=f"Encrypted: {encrypted}")

def on_decrypt():
    encrypted = encrypted_label.cget("text").replace("Encrypted: ", "")
    decrypted = decrypt_password(encrypted.encode(), key)
    decrypted_label.config(text=f"Decrypted: {decrypted}")

# Setting up the window
root = tk.Tk()
root.title("Password Encryption Tool")

key = generate_key()

# Adding widgets
password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.pack()

encrypted_label = tk.Label(root, text="Encrypted: ")
encrypted_label.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.pack()

decrypted_label = tk.Label(root, text="Decrypted: ")
decrypted_label.pack()

root.mainloop()