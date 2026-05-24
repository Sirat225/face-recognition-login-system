import tkinter as tk
import subprocess
import os

def open_register():
    subprocess.Popen(["python", "register/register.py"], shell=True)

def open_login():
    subprocess.Popen(["python", "login/login.py"], shell=True)

def open_trainer():
    subprocess.Popen(["python", "train/trainer.py"], shell=True)

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("Face Recognition Login System")
window.geometry("400x400")
window.configure(bg="#FFDEE9")

title = tk.Label(window, text="Face Recognition Login System", font=("Helvetica", 16, "bold"), bg="#FFDEE9", fg="#333")
title.pack(pady=30)

btn1 = tk.Button(window, text="Register", command=open_register, width=20, height=2, bg="#FFB6C1")
btn1.pack(pady=10)

btn2 = tk.Button(window, text="Login", command=open_login, width=20, height=2, bg="#FFB6C1")
btn2.pack(pady=10)

btn3 = tk.Button(window, text="Train Recognizer", command=open_trainer, width=20, height=2, bg="#FFB6C1")
btn3.pack(pady=10)

btn4 = tk.Button(window, text="Exit", command=exit_app, width=20, height=2, bg="#FFB6C1")
btn4.pack(pady=10)

window.mainloop()