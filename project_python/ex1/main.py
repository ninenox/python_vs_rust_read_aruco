import cv2
import cv2.aruco as aruco
import time

def findArucoMarkers(img, arucoDict, arucoParam, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bboxs, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters=arucoParam)
    #print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs,ids)
cap = cv2.VideoCapture(0)

# Create ArUco dictionary and detector parameters once
MARKER_SIZE = 6
TOTAL_MARKERS = 250
key = getattr(aruco, f'DICT_{MARKER_SIZE}X{MARKER_SIZE}_{TOTAL_MARKERS}')
arucoDict = aruco.Dictionary_get(key)
arucoParam = aruco.DetectorParameters_create()
while True:
    start = time.time()
    success, img = cap.read()
    cimage = img.copy()
    findArucoMarkers(cimage, arucoDict, arucoParam)
    cv2.imshow('img',cimage)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    end = time.time()
    print('Time elapsed : '+str(end - start))
cap.release()
cv2.destroyAllWindows()
