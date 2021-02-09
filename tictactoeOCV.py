import cv2
import numpy as np

frameWidth = 640
frameHeight = 485

fistLine = ((95,180),(554,180))
secondLine = ()
thirdLine = ()
fourthLine = ()

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

while True:
    success, img = cap.read()
    cv2.line(img, (95, 180), (554, 180),(255,0,0),3)
    cv2.line(img,(95,300),(554,300),(255,0,0),3)
    cv2.line(img,(245,60),(245,420),(255,0,0),3)
    cv2.line(img,(395,60),(395,420),(255,0,0),3)
    cv2.imshow("Tic Tac Toe",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break