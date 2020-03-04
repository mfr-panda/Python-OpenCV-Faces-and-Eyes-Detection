import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import numpy as np

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
log.basicConfig(filename='webcam-detect.log',level=log.INFO)

eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

videoCap = cv2.VideoCapture(0)
log_faces = 0
log_eyes = 0

while True:
    if not videoCap.isOpened():
        print('camera unavailable.')
        sleep(5)
        pass

    ret, frame = videoCap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around faces and eyes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    if log_faces= len(faces):
        log_faces = len(faces)
        log.info("FACES: "+str(len(faces))+" at "+str(dt.datetime.now()))

    if log_eyes= len(eyes):
        log_eyes = len(eyes)
        log.info("EYES: "+str(len(eyes))+" at "+str(dt.datetime.now()))

    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('Video', frame)

videoCap.release()
cv2.destroyAllWindows()
