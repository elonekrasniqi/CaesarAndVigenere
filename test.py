import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from functools import partial
import os


def caesar_encrypt(input_text, shift):
    encrypted_text = ""
    for char in input_text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def vigenere_encrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - 65
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result
def vigenere_decrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - 65
            if char.isupper():
                result += chr((ord(char) - 65 - shift + 26) % 26 + 65)









def select_operation(algorithm):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    operation = tk.simpledialog.askstring("Operation", "Enter 'encrypt' or 'decrypt':")
    if operation not in ['encrypt', 'decrypt']:
        messagebox.showerror("Error", "Invalid operation.")
        return

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        messagebox.showerror("Error", "No file selected.")
        return

    save_path = filedialog.askdirectory(title="Select Save Location")
    if not save_path:
        messagebox.showerror("Error", "No save location selected.")
        return

    if algorithm == "Caesar":
        shift = tk.simpledialog.askinteger("Shift Value", "Enter the shift value:")
        if shift is None:
            messagebox.showerror("Error", "No shift value entered.")
            return

        if operation == "encrypt":
            with open(file_path, "r") as file:
                input_text = file.read()
            output_text = caesar_encrypt(input_text, shift)
            output_file_path = os.path.join(save_path, "caesar_encrypted.txt")
        else:
            with open(file_path, "r") as file:
                input_text = file.read()
            output_text = caesar_decrypt(input_text, shift)
            output_file_path = os.path.join(save_path, "caesar_decrypted.txt")

    elif algorithm == "Vigenere":
        key = tk.simpledialog.askstring("Key", "Enter the encryption key:")


        if key is None:
            messagebox.showerror("Error", "No key entered.")
            return
        

        if operation == "encrypt":
            with open(file_path, "r") as file:
                input_text = file.read()
            output_text = vigenere_encrypt(input_text, key)
            output_file_path = os.path.join(save_path, "vigenere_encrypted.txt")

        else:
            
            with open(file_path, "r") as file:
                input_text = file.read()
            output_text = vigenere_decrypt(input_text, key)
            output_file_path = os.path.join(save_path, "vigenere_decrypted.txt")
        