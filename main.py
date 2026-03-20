import cv2
import face_recognition
import os
import json
import numpy as np
import sys

# SETTINGS
DATASET_PATH = "dataset"
DATABASE_PATH = "database/users.json"
MATCH_THRESHOLD = 0.50   # lower = stricter (0.45–0.60 recommended)

# SAFE EXIT FUNCTION
def safe_exit(video):
    print("Closing system...")
    video.release()
    cv2.destroyAllWindows()
    sys.exit(0)

# CHECK PATHS
if not os.path.exists(DATASET_PATH):
    print("ERROR: dataset folder not found")
    sys.exit(1)

if not os.path.exists(DATABASE_PATH):
    print("ERROR: users.json not found")
    sys.exit(1)

# LOAD DATABASE
with open(DATABASE_PATH, "r") as file:
    users = json.load(file)

# LOAD FACE DATASET
known_encodings = []
known_ids = []
print("Loading dataset...")

for filename in os.listdir(DATASET_PATH):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        path = os.path.join(DATASET_PATH, filename)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            print("WARNING: No face found in", filename)
            continue

        encoding = encodings[0]

        person_id = os.path.splitext(filename)[0]
        known_encodings.append(encoding)
        known_ids.append(person_id)
        print("Loaded:", person_id)

if len(known_encodings) == 0:
    print("ERROR: No valid faces in dataset")
    sys.exit(1)
print("Dataset loaded successfully")

# START CAMERA
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("ERROR: Cannot open camera")
    sys.exit(1)

cv2.namedWindow("Face Recognition System", cv2.WINDOW_NORMAL)
print("System started. Press ESC or close window to exit.")

# MAIN LOOP
while True:
    ret, frame = video.read()

    if not ret:
        print("Camera error")
        break

    # Resize for speed
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for encoding, location in zip(face_encodings, face_locations):
        distances = face_recognition.face_distance(known_encodings, encoding)
        best_index = np.argmin(distances)
        best_distance = distances[best_index]

        # Default values
        name = "Unknown"
        age = "-"
        pid = "-"
        color = (0,0,255)  # red for unknown

        # Only accept if distance is safe
        if best_distance < MATCH_THRESHOLD:
            person_key = known_ids[best_index]
            
            if person_key in users:
                name = users[person_key].get("name", "Unknown")
                age = users[person_key].get("age", "-")
                # Support both 'id' and legacy 'PID' keys in the database
                pid = users[person_key].get("id") or users[person_key].get("PID") or person_key
                color = (0,255,0)  # green for known

        # Scale back
        top, right, bottom, left = location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        # Draw box
        cv2.rectangle(frame,
                      (left, top),
                      (right, bottom),
                      color,
                      2)

        # Draw label background
        cv2.rectangle(frame,
                      (left, top - 35),
                      (right, top),
                      color,
                      cv2.FILLED)
        # Show text
        text = f"{name} | Age:{age} | ID:{pid}"

        cv2.putText(frame,
                    text,
                    (left + 5, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255,255,255),
                    2)

    cv2.imshow("Face Recognition System", frame)

    # Exit if ESC pressed
    key = cv2.waitKey(1)
    if key == 27:
        safe_exit(video)

    # Exit if window closed
    if cv2.getWindowProperty("Face Recognition System", cv2.WND_PROP_VISIBLE) < 1:
        safe_exit(video)