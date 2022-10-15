import cv2
import mediapipe
import numpy as np
import time
import HandTrackingModule as htm
import math

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.HandDetector(detectionCon = 0.7)
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.FindHands(img)
    lmList = detector.FindPosition(img, draw = False)
    #print(lmList)

    if len(lmList) != 0:

        fingers = []

        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                #print("Index Finger Open")
                fingers.append(1)
            else:
                fingers.append(0)


    cv2.imshow("FingersCounting", img)
    cv2.waitKey(1)