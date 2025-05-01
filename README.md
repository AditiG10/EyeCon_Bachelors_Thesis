
# 👁️‍🗨️ EyeCon – The Speaker for Paralyzed

**Bachelor's Final Year Project – B.E. in Computer Engineering**  
New Horizon Institute of Technology and Management (University of Mumbai)  
Developed by: Aditi Godbole, Deepika Rao, Komal Pawoolkar  
Guide: Dr. Sanjay Sharma

---

## 🧠 Project Overview

**EyeCon** is an assistive communication system developed for individuals with motor neuron disorders (MND), paralysis, and Locked-In Syndrome (LIS). By detecting eye blinks using standard webcams or smartphone front cameras, the system converts them into textual commands and ultimately speech — enabling communication for those who otherwise cannot express themselves verbally or physically.

---

## 🎯 Motivation

Thousands of individuals across the globe suffer from conditions that impair their ability to communicate, such as ALS, LIS, or spinal injuries. While commercial solutions exist, they are often:

- Hardware-intensive
- Financially inaccessible
- Difficult to use without caregiver assistance

**EyeCon** provides a **low-cost, software-only solution** that can run on any device with a webcam — giving users independence, dignity, and a voice.

---

## 🏗️ System Architecture

The system is divided into three core modules:

1. **Eye Blink Detection Module**  
   - Uses OpenCV, dlib, and facial landmarks to compute Eye Aspect Ratio (EAR)
   - Identifies intentional eye blinks based on thresholds and consecutive frame counts

2. **User Interaction Module**  
   - Displays a virtual keyboard on screen
   - Allows row/column navigation based on blink patterns
   - Records selected characters as text

3. **Text-to-Speech Conversion Module**  
   - Uses Web Speech API to convert selected text into audible speech
   - Provides real-time feedback for the user and caregivers

---

## 💡 Key Technologies

- Python 3.8+
- Flask (Web Framework)
- OpenCV (Computer Vision)
- Dlib (Facial Landmark Detection)
- JavaScript + Web Speech API (Text-to-Speech)
- HTML5 + CSS + Bootstrap (UI Design)
- AJAX (Dynamic updates without reloading)

---

## 🧪 Results

- **Blink Detection Accuracy:** 94%
- **Text Navigation & Selection:** 92% success rate across multiple test subjects
- **Speech Output:** 100% accurate for valid and complete sentences

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/AditiG10/EyeCon_Bachelors_Thesis.git
```

### 2. Set up virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app/main.py
```

---

## 📁 Folder Structure

```
eyecon/
├── app/                 # Backend logic & detection scripts
├── static/              # Haar cascades & runtime files
├── templates/           # HTML templates
├── models/              # shape_predictor_68_face_landmarks.dat
├── video_input/         # Sample videos
├── notebooks/           # Experimentation notebooks
├── dlib_src/            # (Optional) Local dlib build
├── screenshots/         # Placeholder screenshots
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

---

## 🔭 Future Scope

- Detect blinks even under poor lighting or partial face visibility
- Multilingual speech support
- Enhanced keyboard with frequently used phrases
- Integration with cloud for saving communication history
- Support for mobile apps via cross-platform deployment

---

## 📚 Publication

This work was accepted at the **International Conference on Software Engineering and Computer Science (ICSECS)** held in May 2021, Bengaluru, India.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

We thank our mentor **Dr. Sanjay Sharma** and the faculty of the Department of Computer Engineering at **New Horizon Institute of Technology and Management** for their constant support.
