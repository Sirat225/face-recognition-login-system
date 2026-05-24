import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def get_images_and_labels(path):
    image_paths = []
    labels = []
    label_dict = {}
    label_id = 0

    for person_name in os.listdir(path):
        person_folder = os.path.join(path, person_name)
        if not os.path.isdir(person_folder):
            continue
        label_dict[label_id] = person_name
        for img_file in os.listdir(person_folder):
            image_path = os.path.join(person_folder, img_file)
            img = Image.open(image_path).convert('L')
            img_np = np.array(img, 'uint8')
            image_paths.append(img_np)
            labels.append(label_id)
        label_id += 1

    return image_paths, labels, label_dict

faces, ids, label_dict = get_images_and_labels("data")
recognizer.train(faces, np.array(ids))
os.makedirs("trainer", exist_ok=True)
recognizer.save("trainer/recognizer.yml")

with open("trainer/labels.txt", "w") as f:
    for k, v in label_dict.items():
        f.write(f"{k},{v}\n")

print("Training complete.")