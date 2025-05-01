# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2

def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])

	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)

	# return the eye aspect ratio
	return ear


# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold
EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_FRAMES = 3

# initialize the frame counters and the total number of blinks
COUNTER = 0
TOTAL = 0


# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\deepi\Downloads\blinkToText-master\shape_predictor_68_face_landmarks.dat")


# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


# start the video stream thread
print("[INFO] starting video stream thread...")
vs = VideoStream(src=0).start()


fileStream = False
time.sleep(1.0)


face_cascade = cv2.CascadeClassifier(r'C:\Users\deepi\Downloads\blinkToText-master\static\haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(r'C:\Users\deepi\Downloads\blinkToText-master\static\haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)
count = 0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        roi_grayLeft = gray[y:y+h, x:x+w//2]
        roi_grayRight = gray[y:y+h, x+w//2:x+w]
        leftEye = eye_cascade.detectMultiScale(roi_grayLeft)
        rightEye = eye_cascade.detectMultiScale(roi_grayRight)
        if len(leftEye)==0 and len(rightEye)==0:
            count=count+1
            print(count)
            file=open(r"C:\Users\deepi\Downloads\blinkToText-master\haze.txt","w")#("haze.txt","w")
            file.write("1")
            file.close()
            
        for (ex,ey,ew,eh) in rightEye:
                cv2.rectangle(roi_color,(ex+w//2,ey),(ex+ew+w//2,ey+eh),(255,255,0),2)
        for (ex,ey,ew,eh) in leftEye:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(25) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
