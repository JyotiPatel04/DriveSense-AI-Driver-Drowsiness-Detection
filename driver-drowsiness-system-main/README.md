# driver-drowsiness-system
# Driver Drowsiness Detection System (Full-Stack AI Project)

---

# 📌 Overview

This project is a **production-ready AI-powered driver monitoring system** that detects drowsiness in real-time and enhances safety using alerts, SOS, and live tracking.

It integrates:

*  Machine Learning (TensorFlow/Keras)
*  OpenCV + Haar Cascades
*  YOLOv8 (Object Detection)
*  FastAPI Backend
*  React Frontend
*  Firebase Authentication
*  MongoDB Logging
*  SOS + Live Location

---

# 🏗️ COMPLETE PROJECT STRUCTURE 

```bash
driver-drowsiness-system/
│
├── training/                     # (YOUR EXISTING)
│   ├── dataset/
│   │   ├── awake/
│   │   ├── drowsy/
│   ├── train_model.py
│   ├── drowsiness_model.h5
│
├── ai_module/                   # (YOUR CORE LOGIC)
│   ├── detect.py
│   ├── features.py
│   ├── yolo_detector.py
│   ├── utils.py
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_default.xml
│   ├── alarm.wav
│
├── backend/                     # (API LAYER)
│   ├── main.py
│   ├── firebase_config.py
│   ├── database.py
│   ├── routes/
│   │   ├── logs.py
│   │   ├── sos.py
│
├── frontend/                    # (UI)
│   ├── src/
│   │   ├── firebase.js
│   │   ├── App.js
│   │   ├── pages/
│   │   │   ├── Login.js
│   │   │   ├── Signup.js
│   │   │   ├── Dashboard.js
│   │   │   ├── Drive.js
│   │   │   ├── About.js
│
├── models/
│   ├── yolov8n.pt
│
├── logs/
│   ├── log.txt
│
├── requirements.txt
└── README.md
```

---

# 🔄 SYSTEM FLOW (END-TO-END)

```text
User → Login (Firebase)
        ↓
Dashboard
        ↓
Start Driving
        ↓
Backend triggers detect.py
        ↓
Camera starts
        ↓
AI Processing:
   - Face Detection
   - Eye Detection
   - ML Prediction
   - YOLO (Phone)
        ↓
Decision Engine
        ↓
Score Update
        ↓
 ┌───────────────┬───────────────┬───────────────┐
 │               │               │               │
Awake        Drowsy        Phone Use       Head Tilt
 │               │               │               │
 ↓               ↓               ↓               ↓
Reduce Score  Increase Score  Increase Score  Increase Score
        ↓
Threshold Crossed?
        ↓
YES → Alarm + Notification + Log + SOS
```

---

# 🧠 AI + COMPUTER VISION FLOW

```text
[Webcam Frame]
      ↓
[Face Detection - Haar]
      ↓
[Eye Detection]
      ↓
[Image Preprocessing]
      ↓
[ML Model Prediction]
      ↓
[YOLO Detection (Phone)]
      ↓
[Hybrid Decision Logic]
      ↓
[Output: Status + Score + Safety %]
```

---

# 🔐 AUTHENTICATION FLOW (FIREBASE)

```text
User → React Login Page
        ↓
Firebase Authentication
        ↓
Returns Token
        ↓
Frontend sends Token → FastAPI
        ↓
Backend Verifies Token
        ↓
Access Granted
```

---

# 🗄️ DATABASE FLOW (MONGODB)

```text
detect.py → FastAPI → MongoDB

Stored Data:
- score
- status
- timestamp
- SOS alerts
- driver location
```

---

# 🚨 SOS FLOW

```text
Driver clicks SOS
      ↓
Browser fetches GPS location
      ↓
Send to FastAPI
      ↓
Stored in MongoDB
      ↓
(Extendable → SMS / Emergency Call)
```

---

# 🖥️ UI / UX SNAPSHOTS (REPRESENTATION)

---

## 🔐 Login Page

```text
+------------------------+
|  Driver Safety System  |
|------------------------|
| Email: _____________   |
| Password: __________   |
|                        |
| [ Login ]              |
| [ Signup ]             |
+------------------------+
```

---

## 📊 Dashboard

```text
+---------------------------+
| Welcome, Driver 🚗        |
|---------------------------|
| [ Start Driving ]         |
| [ About System ]          |
| [ View Logs ]             |
| [ SOS Emergency ]         |
+---------------------------+
```

---

## 🚗 Drive Mode

```text
+----------------------------------+
|  LIVE CAMERA FEED               |
|  -----------------------------  |
|  Face Box + Status              |
|                                 |
|  Score: 6                       |
|  Safety: 82%                    |
|                                 |
|  🚨 SOS BUTTON                  |
+----------------------------------+
```

---

##  ALERT SYSTEM

```text
 DROWSINESS DETECTED
 Alarm Triggered
 Notification Sent
 Location Ready for SOS
```

---

# ⚙️ INSTALLATION & SETUP

---

## 1️⃣ Clone Project

```bash
git clone <your-repo>
cd driver-drowsiness-system
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
npm install
```

---

## 3️⃣ Run Backend

```bash
cd backend
uvicorn main:app --reload
```

---

## 4️⃣ Run Frontend

```bash
cd frontend
npm start
```

---

## 5️⃣ Run AI Module

```bash
python ai_module/detect.py
```

---

# 🔑 FIREBASE SETUP

1. Go to Firebase Console
2. Create project
3. Enable Email/Password login
4. Download `serviceAccountKey.json`
5. Add config in:

   * `frontend/src/firebase.js`
   * `backend/firebase_config.py`

---

# 🗄️ MONGODB SETUP

```bash
Install MongoDB locally OR use MongoDB Atlas
Update connection string in database.py
```

---

# 🔔 NOTIFICATIONS

* Uses browser notification API
* Triggered when driver becomes drowsy

---

# 🚀 FEATURES SUMMARY

| Feature                 | Status |
| ----------------------- | ------ |
| ML Drowsiness Detection | ✅      |
| Eye Tracking            | ✅      |
| YOLO Phone Detection    | ✅      |
| Alarm Alert             | ✅      |
| Firebase Auth           | ✅      |
| MongoDB Logging         | ✅      |
| SOS System              | ✅      |
| Live Location           | ✅      |
| Full Stack UI           | ✅      |

---

#  RESUME DESCRIPTION

**Driver Drowsiness Detection System (AI + Full Stack)**

* Developed a real-time driver monitoring system using OpenCV, TensorFlow, and YOLOv8.
* Implemented Firebase Authentication and MongoDB logging.
* Built a full-stack dashboard with React and FastAPI.
* Integrated SOS emergency alert system with live location tracking.

---

# 💡 FUTURE IMPROVEMENTS

*  Mobile App (React Native)
*  Cloud Deployment (AWS / GCP)
*  Analytics Dashboard
*  Model Accuracy Enhancement
*  Vehicle Hardware Integration

---

# ⭐ FINAL NOTE

This is a **complete production-level AI system** combining:

* Computer Vision
* Deep Learning
* Full Stack Development
* Real-time Processing

---

<!-- Contributors -->
 Charu Awasthi : https://github.com/Charu19awasthi/driver-drowsiness-system
