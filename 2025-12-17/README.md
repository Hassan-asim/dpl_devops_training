<h1 align="center">dpl_devops_training</h1>

<h3 align="center" style="color:#007bff;">Daily DevOps Practice • New AWS Architecture Course & Rebel Capture App</h3>

---

## 🎯 Objective Recap
- Started a new **AWS architecture-focused course**, progressing through multiple parts and capturing each milestone.
- Began work on the **Rebel Capture – DPL Webcam Prototype** task, reviewing the repo, flows, and local run instructions.
- Captured screenshots of the new React + FastAPI camera app screens (splash, home, camera feed, preview, success).

---

## 🛠️ Study & Dev Environment
- **Host OS:** Windows
- **Editor:** Visual Studio Code
- **Terminal:** PowerShell (Windows PowerShell v5.1)
- **Notes & Evidence:** Screenshots stored in `2025-12-17/images/`.

---

## 📚 New AWS Architecture Course Progress
- Kicked off a new AWS architecture course and moved through sequential lesson parts:
  - Part 1: ![AWS architecture course part 1](./images/aws%20architecture%20course%20part%201.png)
  - Part 2: ![AWS architecture course part 2](./images/aws%20architecture%20course%20part%202.png)
  - Part 3: ![AWS architecture course part 3](./images/aws%20architecture%20course%20part%203.png)
  - Part 4: ![AWS architecture course part 4](./images/aws%20architecture%20course%20part%204.png)
  - Part 5: ![AWS architecture course part 5](./images/aws%20architecture%20course%20part%205.png)
  - Part 6: ![AWS architecture course part 6](./images/aws%20architecture%20course%20part%206.png)
  - Part 7: ![AWS architecture course part 7](./images/aws%20architecture%20course%20part%207.png)
  - Part 8: ![AWS architecture course part 8](./images/aws%20architecture%20course%20part%208.png)
  - Part 9: ![AWS architecture course part 9](./images/aws%20architecture%20course%20part%209.png)
  - Part 10: ![AWS architecture course part 10](./images/aws%20architecture%20course%20part%2010.png)
  - Part 11: ![AWS architecture course part 11](./images/aws%20architecture%20course%20part%2011.png)
  - Part 12: ![AWS architecture course part 12](./images/aws%20architecture%20course%20part%2012.png)
  - Part 13: ![AWS architecture course part 13](./images/aws%20architecture%20course%20part%2013.png)
  - Part 14: ![AWS architecture course part 14](./images/aws%20architecture%20course%20part%2014.png)
  - Part 15: ![AWS architecture course part 15](./images/aws%20architecture%20course%20part%2015.png)
  - Part 16: ![AWS architecture course part 16](./images/aws%20architecture%20course%20part%2016.png)
- Also started an additional **STS-focused course segment**:
  - Part 1: ![STS course part 1](./images/STS%20course%20part%201.png)

---

## 📸 Rebel Capture – DPL Webcam Prototype (Task)

**Repo:** [`rebel_photo_capture_app`](https://github.com/Hassan-asim/rebel_photo_capture_app)  
Rebel Capture is a simplified but fully functional webcam capture prototype built at **DPL**. It provides:
- Photo capture from a Logitech HD Pro C920 (or any webcam).
- Short video recording.
- A Rebel logo watermark baked into captured photos.
- Upload of photos and videos to a **FastAPI** backend, which stores them into `images/` and `videos/` folders.  
Source: [`rebel_photo_capture_app` README](https://github.com/Hassan-asim/rebel_photo_capture_app).

### 🧱 High-Level Architecture (from the repo README)
- **Frontend (React, Create React App):**
  - Screens: Splash → Home → Camera → Preview → Confirmation.
  - Live webcam feed with **Photo / Video** toggle and a large shutter button.
  - Photo capture via `MediaDevices.getUserMedia` → `<video>` → `<canvas>` → Base64 PNG.
  - Video recording via `MediaRecorder` → WebM blob → Base64.
  - Watermark: `logo.png` composited into the bottom-right of photos.
- **Backend (FastAPI):**
  - `GET /health` – health check.
  - `POST /upload` – accepts Base64 image data, saves PNG into `images/`.
  - `POST /upload-video` – accepts Base64 WebM, saves clips into `videos/`.
  - Uses `pydantic`, `base64`, `datetime`, and runs via `uvicorn`.
  - Storage layout:
    - `images/` – `capture_YYYYMMDDHHMMSS.png`
    - `videos/` – `clip_YYYYMMDDHHMMSS.webm`

### 🖥️ Local Run Notes (from the repo README)
- **Backend:**
  - `cd backend`
  - `python -m pip install -r requirements.txt`
  - `python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
  - Health check at `http://localhost:8000/health` should return `{"status":"healthy"}`.
- **Frontend:**
  - `cd frontend`
  - `npm install`
  - `npm start`
  - Main UI at `http://localhost:3000` (camera access works on `localhost`/`127.0.0.1` or HTTPS).  
Reference: [`rebel_photo_capture_app` README](https://github.com/Hassan-asim/rebel_photo_capture_app).

### 📸 App UI Evidence
- Splash screen: ![Rebel Capture splash](./images/capture%20app%20splash%20screen%20.png)
- Home page: ![Rebel Capture home](./images/capture%20app%20home%20page%20.png)
- Live camera feed: ![Rebel Capture camera feed](./images/capture%20app%20camera%20feed.png)
- Image preview screen: ![Rebel Capture image preview](./images/capture%20app%20img%20preview%20screen.png)
- Success message screen: ![Rebel Capture success message](./images/capture%20app%20sucssess%20msg%20screen.png)

---

## ✅ Daily Summary
- Started and advanced through multiple parts of a new **AWS architecture** course, plus an STS segment, capturing each milestone as evidence.
- Reviewed and documented the **Rebel Capture – DPL Webcam Prototype** stack (React + FastAPI), its endpoints, storage layout, and local run steps using the official repo README.
- Captured and stored screenshots of the new **Rebel Capture** UI screens (splash, home, camera, preview, and success) to document progress on the assigned task.

Made by Sufi Hassan Asim — 2025-12-17



