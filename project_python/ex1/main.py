import cv2
import cv2.aruco as aruco
import numpy as np
import os
import time

def findArucoMarkers(img, markerSize = 6, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    #print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs,ids) 
cap = cv2.VideoCapture(0)
while True:
    start = time.time()
    success, img = cap.read()
    cimage = img.copy()
    findArucoMarkers(cimage)
    cv2.imshow('img',cimage)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    end = time.time()
    print('Time elapsed : '+str(end - start))
cap.release()
cv2.destroyAllWindows()