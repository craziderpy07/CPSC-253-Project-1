import customtkinter
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("CPSC 253 Project 1")
root.iconbitmap(r"C:\Users\zz-teto\CPSC-253-Project-1\kirby.ico")
kirby_icon = tk.PhotoImage(file=r"C:\Users\zz-teto\CPSC-253-Project-1\kirby-icon-removebg-preview (1).png")
root.iconphoto(False, kirby_icon)
root.geometry("500x350")

def login():
    print("test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()