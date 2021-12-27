# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:08:22 2021

@author: bnlad
"""

import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\bnlad\Desktop\Face Detection\From Image\haarcascade_frontalface_default.xml')
img = cv2.imread(r'C:\Users\bnlad\Desktop\Face Detection\From Image\binil.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3,
        minNeighbors=2,
        minSize=(30, 30))
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()