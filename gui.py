from tkinter import *
from tkinter import ttk
import time
from tkinter import filedialog       

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:/", filetypes=[("Text Files", "*.txt")])
    file = open(filepath, 'r')
    print(file.read())
    file.close()

def step():
    for x in range(10):
        my_progress['value'] += 10
        root.update_idletasks()
        time.sleep(0.5)

root = Tk()
root.title("CPSC 253 Project 1")
root.iconbitmap(r"C:\Users\zz-teto\CPSC-253-Project-1\kirby.ico")
root.geometry("500x250")
root.resizable(False, False)

Frame(root, bg="pink").pack(fill="both", expand=TRUE)
my_label = Label(root, text="CPSC 253 Project 1", font=("System", 25), fg="white", bg="pink")
my_label.place(relx=0.5, rely=0.25, anchor="center")

decrypt_button = Button(text="Decrypt", pady=10, padx=10, activebackground="pink2", 
                   activeforeground="white", bg="white", fg="pink", overrelief="raised", command=openFile)
decrypt_button.place(relx=0.6, rely=0.5, anchor="w")

encrypt_button = Button(text="Encrypt", pady=10, padx=10, activebackground="pink2", 
                   activeforeground="white", bg="white", fg="pink", overrelief="raised", command=openFile)
encrypt_button.place(relx=0.4, rely=0.5, anchor="e")

my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=250, mode='determinate')
my_progress.pack(pady=10)

root.mainloop()