from tkinter import *
from tkinter import filedialog    
from tkinter import ttk
import os

def key():
    try:
        my_key = int(key_entry.get())
        return my_key
    except BaseException:
        print("The key can only be an integer.")

def encrypt(text, key):
    encrypted_text = ''.join([chr(ord(char) + key) for char in text])  
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ''.join([chr(ord(char) - key) for char in text])
    return decrypted_text

def decryptFile():
    filepath = filedialog.askopenfilename(initialdir="C:/")
    my_file = os.path.basename(filepath)
    file_size = os.path.getsize(my_file)

    if (file_size == 0) :
        print(f"The file {my_file} is empty. There is nothing to decrypt!")
    else :
        if filepath.endswith('.txt'):
            try:
                with open(filepath, 'r') as file:
                    lines = file.readlines()

                with open("Decryption.txt", 'w') as file:
                    for line in lines:
                        file.write(decrypt(line, key()))
            except BaseException:
                my_file = os.path.basename(filepath)
                print(f"Error: {my_file} is not found!")
        else:
            print(f"The file {my_file} is not a text file.")

def encryptFile():
    filepath = filedialog.askopenfilename()
    my_file = os.path.basename(filepath)
    file_size = os.path.getsize(my_file)

    if(file_size == 0) :
        print(f"The file {my_file} is empty. There is nothing to encrypt!")
    else :
        if filepath.endswith('.txt'):
            try:
                with open(filepath, 'r') as file:
                    lines = file.readlines()

                with open("Encryption.txt", 'w') as file:
                    for line in lines:
                        file.write(encrypt(line, key()))
            except BaseException:
                print(f"Error: {my_file} is not found!")
        else:
            print(f"The file {my_file} is not a text file.")
                         
root = Tk()
root.title("CPSC 253 Project 1")
root.iconbitmap(r"kirby.ico")
root.geometry("500x250")
root.resizable(False, False)

Frame(root, bg="pink").pack(fill="both", expand=TRUE)
title_label = Label(root, text="CPSC 253 Project 1", font=("System", 25), fg="white", bg="pink")
title_label.place(relx=0.5, rely=0.25, anchor="center")

decrypt_button = Button(text="Decrypt", pady=10, padx=10, activebackground="pink2", 
                   activeforeground="white", bg="white", fg="pink", overrelief="raised", command=decryptFile)
decrypt_button.place(relx=0.6, rely=0.5, anchor="w")

encrypt_button = Button(text="Encrypt", pady=10, padx=10, activebackground="pink2", 
                   activeforeground="white", bg="white", fg="pink", overrelief="raised", command=encryptFile)
encrypt_button.place(relx=0.4, rely=0.5, anchor="e")

number_label = Label(root, text="Enter your key (integer):", font=("System", 5), fg="white", bg="pink")
number_label.place(relx=0.58, rely=0.73, anchor="e")

number_button = Button(root, text="Enter", activebackground="pink2", 
                   activeforeground="white", bg="white", fg="pink", overrelief="raised", command=key)
number_button.place(relx=0.63, rely=0.85, anchor="w")

key_entry = Entry(root,font=("System"), width=20)
key_entry.place(relx=0.43, rely=0.85, anchor="center")

root.mainloop()