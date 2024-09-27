from tkinter import *
from tkinter import filedialog    
import os

#Takes in the user's key
def key():
    try:
        my_key = int(key_entry.get())
        return my_key
    #To prevent anything that is not a number from being used as the key
    except BaseException:
        print("The key can only be an integer.")

#Encrypts the .txt file
def encrypt(text, key):
    encrypted_text = ''.join([chr(ord(char) + key) for char in text])  
    return encrypted_text

#Decrypts the .txt file
def decrypt(text, key):
    decrypted_text = ''.join([chr(ord(char) - key) for char in text])
    return decrypted_text

#Opens the file to decrypt
def decryptFile():
    filepath = filedialog.askopenfilename(initialdir="C:/")
    #Presents the file as its name without the directory attached
    my_file = os.path.basename(filepath)
    file_size = os.path.getsize(my_file)

    #Checks to see if the .txt file is empty
    if (file_size == 0) :
        print(f"The file {my_file} is empty. There is nothing to decrypt!")
    else :
        #Checks to see if the file is a .txt file
        if filepath.endswith('.txt'):
            try:
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                
                #Generates the decrypted .txt file
                with open("Decryption.txt", 'w') as file:
                    for line in lines:
                        file.write(decrypt(line, key()))
            #To prevent errors if the file is a .txt file, but has issues
            except BaseException:
                my_file = os.path.basename(filepath)
                print(f"Error: {my_file} is not found!")
        else:
            print(f"The file {my_file} is not a text file.")

#Opens the file to encrypt
def encryptFile():
    filepath = filedialog.askopenfilename()
    #Presents the file as its name without the directory attached
    my_file = os.path.basename(filepath)
    file_size = os.path.getsize(my_file)

    #Checks to see if the .txt file is empty
    if(file_size == 0) :
        print(f"The file {my_file} is empty. There is nothing to encrypt!")
    else :
        #Checks to see if the file is a .txt file
        if filepath.endswith('.txt'):
            try:
                with open(filepath, 'r') as file:
                    lines = file.readlines()

                #Generates the encrypted .txt file
                with open("Encryption.txt", 'w') as file:
                    for line in lines:
                        file.write(encrypt(line, key()))
            #To prevent errors if the file is a .txt file, but has issues
            except BaseException:
                print(f"Error: {my_file} is not found!")
        else:
            print(f"The file {my_file} is not a text file.")

#GUI
root = Tk()
root.title("CPSC 253 Project 1")
root.iconbitmap(r"kirby.ico")
root.geometry("500x250")
root.resizable(False, False)

#CPSC 253 Project 1 title
Frame(root, bg="pink").pack(fill="both", expand=TRUE)
title_label = Label(root, text="CPSC 253 Project 1", font=("System", 25), fg="white", bg="pink")
title_label.place(relx=0.5, rely=0.25, anchor="center")

#Decrypt button
decrypt_button = Button(text="Decrypt", pady=10, padx=10, activebackground="pink2", 
                   activeforeground="white", bg="white", fg="pink", overrelief="raised", command=decryptFile)
decrypt_button.place(relx=0.6, rely=0.5, anchor="w")

#Encrypt button
encrypt_button = Button(text="Encrypt", pady=10, padx=10, activebackground="pink2", 
                   activeforeground="white", bg="white", fg="pink", overrelief="raised", command=encryptFile)
encrypt_button.place(relx=0.4, rely=0.5, anchor="e")

#"Enter your key (integer): "
key_label = Label(root, text="Enter your key (integer):", font=("System", 5), fg="white", bg="pink")
key_label.place(relx=0.58, rely=0.73, anchor="e")

#Enters the user's input for the key
enter_button = Button(root, text="Enter", activebackground="pink2", 
                   activeforeground="white", bg="white", fg="pink", overrelief="raised", command=key)
enter_button.place(relx=0.63, rely=0.85, anchor="w")

#The area where the user enters in the key
key_entry = Entry(root,font=("System"), width=20)
key_entry.place(relx=0.43, rely=0.85, anchor="center")

root.mainloop()