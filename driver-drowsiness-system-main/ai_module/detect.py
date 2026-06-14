import cv2
import numpy as np
import threading
import os
import requests
from tensorflow.keras.models import load_model

# =========================
# PATHS (keep your structure)
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "training", "drowsiness_model.h5")
FACE_PATH = os.path.join(BASE_DIR, "ai_module", "haarcascade_frontalface_default.xml")
EYE_PATH = os.path.join(BASE_DIR, "ai_module", "haarcascade_eye.xml")
ALARM_PATH = os.path.join(BASE_DIR, "ai_module", "alarm.wav")

# =========================
# LOAD
# =========================
model = load_model(MODEL_PATH)
face_cascade = cv2.CascadeClassifier(FACE_PATH)
eye_cascade = cv2.CascadeClassifier(EYE_PATH)

# =========================
# GLOBALS
# =========================
score = 0
alarm_on = False

# =========================
# FUNCTIONS
# =========================
def play_alarm():
    global alarm_on
    if alarm_on:
        os.system(f'start {ALARM_PATH}')   # ✅ reliable for Windows
        alarm_on = False

def send_data(score):
    try:
        requests.post(
            "http://127.0.0.1:8000/drowsiness",
            json={"score": score, "status": "DROWSY"}
        )
    except:
        pass

# =========================
# MAIN
# =========================
def detect():
    global score, alarm_on

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera not working")
        return

    print("🚀 Detection started...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        status = "AWAKE"

        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]

            # =========================
            # ML PREPROCESS
            # =========================
            face_resized = cv2.resize(face_img, (64, 64))
            face_resized = face_resized / 255.0
            face_resized = np.reshape(face_resized, (1, 64, 64, 3))

            prediction = model.predict(face_resized, verbose=0)

            # DEBUG (IMPORTANT)
            awake_prob = prediction[0][0]
            drowsy_prob = prediction[0][1]

            print(f"A:{awake_prob:.2f} D:{drowsy_prob:.2f}")

            # =========================
            # HAAR EYES
            # =========================
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            # =========================
            # IMPROVED HYBRID LOGIC
            # =========================
            if (drowsy_prob > 0.5 and len(eyes) == 0):
                score += 2
                status = "DROWSY"
            elif len(eyes) == 0:
                score += 1
                status = "SLEEPY"
            else:
                score = max(0, score - 1)
                status = "AWAKE"

            # DRAW FACE BOX
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
            cv2.putText(frame, status, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        # =========================
        # ALERT SYSTEM
        # =========================
        if score > 5:   # lowered threshold
            cv2.putText(frame, "🚨 DROWSINESS ALERT!", (80,100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)

            if not alarm_on:
                alarm_on = True
                threading.Thread(target=play_alarm).start()
                send_data(score)

        # SCORE DISPLAY
        cv2.putText(frame, f"Score: {score}", (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.imshow("Driver Monitor", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# =========================
# RUN
# =========================
if __name__ == "__main__":
    detect()