import cv2
import os
import tkinter as tk
from tkinter import simpledialog

def capture_images(username):
    user_folder = f"data/{username}"
    os.makedirs(user_folder, exist_ok=True)
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    count = 0

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"{user_folder}/{count}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("Registering Face", img)
        if cv2.waitKey(1) == 27 or count >= 30:
            break

    cam.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.withdraw()
username = simpledialog.askstring("Register", "Enter username:")
if username:
    capture_images(username)