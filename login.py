import cv2

def load_labels(file_path):
    label_dict = {}
    with open(file_path, "r") as f:
        for line in f:
            key, name = line.strip().split(',')
            label_dict[int(key)] = name
    return label_dict

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/recognizer.yml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
labels = load_labels("trainer/labels.txt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        id_, conf = recognizer.predict(gray[y:y+h, x:x+w])
        name = labels.get(id_, "Unknown")
        color = (0, 255, 0) if conf < 70 else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, f"{name} ({int(conf)})", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Login Face Recognition", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()