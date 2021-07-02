import cv2
import dlib
import imutils
import time
import numpy as np


img = cv2.imread("yoona.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread("suzy.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

t1 = time.time()

detector = dlib.get_frontal_face_detector()
t2 = time.time()
print("Detection time: ", t2 - t1)
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
print("landmark time: ", time.time() - t2)
# Face 1
faces = detector(img_gray)
for face in faces:
    landmarks = predictor(img_gray, face)
    landmarks_points = []
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        landmarks_points.append((x, y))

    # drawing landmark points
    for (x, y) in landmarks_points:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    
    points = np.array(landmarks_points, np.int32)
    print(len(points))
    convexhull = cv2.convexHull(points)



img = imutils.resize(img, width=300)
cv2.imshow("Yoona", img)
cv2.waitKey(0)

