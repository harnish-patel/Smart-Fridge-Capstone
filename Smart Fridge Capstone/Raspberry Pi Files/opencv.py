import os
import cv2
import numpy as np
import sys
import glob
import importlib.util
import firebase_admin

from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
from picamera import PiCamera
from time import sleep

# globals
camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 0
imH = 640
imW = 480
height = 416
width = 416
threshold = 0.5

# init

cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {'databaseURL': 'https://test-fridge-default-rtdb.firebaseio.com/'})
firebase_admin.initialize_app(cred, {'databaseURL': 'https://smartfridgeapp-5d119-default-rtdb.firebaseio.com/'})

ref = db.reference('Fridge/')
food_ref = ref.child('food')
food_ref.set({})
non_food = ref.child('non_food')
non_food.set({})

weightsPath = '/home/pi/tflite1/yolov4-obj_best.weights'
cfgPath = '/home/pi/tflite1/yolov4-obj.cfg'
namesPath = '/home/pi/tflite1/obj.names'
imagePath = '/home/pi/tflite1/test.jpg'

# take photo
# camera.start_preview()
# sleep(10)
# camera.capture(imagePath)
# camera.stop_preview()

# init detection model
yolo = cv2.dnn.readNet(weightsPath, cfgPath)

labels = []

with open(namesPath, 'r') as f:
    labels = f.read().splitlines()
    
print(labels)

while(1):
    # take photo
    camera.start_preview()
    sleep(5)
    camera.capture(imagePath)
    camera.stop_preview()

    # prep images
    img = cv2.imread(imagePath)
    img_blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
    yolo.setInput(img_blob)

    # feed detection
    outputLayerName = yolo.getUnconnectedOutLayersNames()
    layerOutput = yolo.forward(outputLayerName)

    boxes = []
    scores = []
    classes = []

    for output in layerOutput:
        for detection in output:
            score = detection[5:]
            class_id = np.argmax(score)
            confidence = score[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[0]*height)
                w = int(detection[0]*width)
                h = int(detection[0]*height)
            
                x = int(center_x - w/2)
                y = int(center_y - h/2)
            
                boxes.append([x,y,w,h])
                scores.append(float(confidence))
                classes.append(class_id)

    a = 0
    o = 0
    b = 0
    c = 0
    t = 0
    p = 0

    #draw bounding boxes
    indexes = cv2.dnn.NMSBoxes(boxes, scores, 0.5, 0.9)
    font = cv2.FONT_HERSHEY_PLAIN
    colours = np.random.uniform(0, 255, size = (len(boxes), 3))

    for i in indexes.flatten():
        x,y,w,h = boxes[i]
    
        label = str(labels[classes[i]])
        scor = str(round(scores[i], 2))
        colour = colours[i]
        
        cv2.rectangle(img, (x,y), (x+w, y+h), colour, 1)
        cv2.putText(img, label +" "+ scor, (x,y+20), font, 2, (0,0,0), 2)
    
        # update counts
        if label == 'Apple':
            a = a + 1
        if label == 'Orange':
            o = o + 1
        if label == 'Banana':
            b = b + 1
        if label == 'Carrot':
            c = c + 1
        if label == 'Tomato':
            t = t + 1
        if label == 'Mobile_phone':
            p = p + 1

    # write to database
    print('Apples: ' + str(a))
    print('Oranges: ' + str(o))
    print('Bananas: ' + str(b))
    print('Carrots: ' + str(c))
    print('Tomatoes: ' + str(t))

    food_ref.set({
        'apple': a,
        'orange': o,
        'banana': b,
        'carrot': c,
        'tomato': t
    })
    
    if p > 0:
        print('hey bro get your phone out of the fridge')
        non_food.set({'phone': p})
    
    cv2.imshow('Object detector', img)
    if cv2.waitKey(0) == ord('q'):
        break