import cv2
import mediapipe as mp
import numpy as np
import time
import pygame
import random

# ---------------- AUDIO SETUP ----------------
pygame.mixer.init()

# Background music
pygame.mixer.music.load("music/gym_music.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# Motivation clips
motivation_clips = [
    "voice/lightweight_baby.mp3",
    "voice/yeah_buddy.mp3",
    "voice/one_more_rep.mp3"
]

def play_motivation():
    clip = pygame.mixer.Sound(random.choice(motivation_clips))
    clip.set_volume(1.0)
    clip.play()

# ---------------- POSE SETUP ----------------
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# ---------------- VARIABLES ----------------
count = 0
stage = None
last_rep_time = time.time()
start_time = time.time()

body_weight = 70  # CHANGE THIS (kg)
MET = 8

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - \
              np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = abs(radians * 180.0 / np.pi)

    if angle > 180:
        angle = 360 - angle
    return angle

# ---------------- MAIN LOOP ----------------
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    try:
        landmarks = results.pose_landmarks.landmark

        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        angle = calculate_angle(shoulder, elbow, wrist)

        if angle < 90:
            stage = "down"

        if angle > 160 and stage == "down":
            stage = "up"
            count += 1
            last_rep_time = time.time()

        # STRUGGLE DETECTION
        if time.time() - last_rep_time > 5 and count > 0:
            play_motivation()
            last_rep_time = time.time()

        # CALORIES
        elapsed_minutes = (time.time() - start_time) / 60
        calories = (MET * body_weight * elapsed_minutes) / 60

        # DISPLAY
        cv2.putText(image, f'Push-ups: {count}', (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 3)

        cv2.putText(image, f'Calories: {calories:.2f}', (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 200, 255), 3)

    except:
        pass

    mp_draw.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow("AI Push-up Coach", image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
pygame.mixer.music.stop()
cv2.destroyAllWindows()
-