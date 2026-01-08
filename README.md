



## 🏋️ AI Push-Up Coach with Real-Time Feedback

An AI-powered push-up counter that uses **computer vision** to detect body posture, count push-ups, estimate calories burned, and play **motivational audio** when the user struggles — all in real time using a webcam.

---

## 🚀 Features

* Real-time push-up detection using webcam
* Accurate rep counting using elbow angle analysis
* Struggle detection (plays motivation if user pauses)
* Live calorie burn estimation
* Background gym music + motivational voice clips
* On-screen stats display (reps + calories)

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * OpenCV
  * MediaPipe
  * NumPy
  * Pygame
  * Time
  * Random

---

## 📂 Project Structure

```
AI-Pushup-Coach/
│
├── pushup_counter.py        # Main application
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
│
├── music/
│   └── gym_music.mp3
│
├── voice/
    ├── lightweight_baby.mp3
    ├── yeah_buddy.mp3
    └── one_more_rep.mp3


```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/vedant4X/AI-Pushup-Coach.git
cd AI-Pushup-Coach
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the project

```
python pushup_counter.py
```

📌 **Press `Q` to quit the application**

---

## 📦 requirements.txt

```
opencv-python
mediapipe
numpy
pygame
```

---

## 🧠 How It Works (Simple Explanation)

1. Webcam captures live video
2. MediaPipe detects body landmarks
3. Elbow angle is calculated frame-by-frame
4. Push-up counted when angle crosses thresholds
5. If user pauses too long → motivation audio plays
6. Calories estimated using MET formula

---

## 📊 Calories Calculation

```
Calories = (MET × Body Weight × Time) / 60
```

* MET for push-ups ≈ **8**
* Body weight is configurable in code

---

## 🎯 Use Cases

* Home workouts
* Fitness motivation
* AI + Computer Vision learning project
* Resume / internship showcase

---

## 🧩 Future Improvements

* Android app version
* Multiple exercise detection
* Voice-guided coaching
* Cloud workout history
* User profile support

---

## 👤 Author

**Vedant**
Computer Engineering Student

---

## 📜 License

This project is licensed under the **MIT License**.
Free to use, modify, and distribute.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---

