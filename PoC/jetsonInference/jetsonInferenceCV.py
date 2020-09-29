import jetson.inference
import jetson.utils

import cv2
import numpy as np


# Cargamos el model de deteccion
net = jetson.inference.detectNet("ssd-inception-v2", threshold=0.4)



cap = cv2.VideoCapture("../videos/main.avi")
cap2 = cv2.VideoCapture("../videos/side1.avi")
cap3 = cv2.VideoCapture("../videos/side2.avi")

while True:
	# Recojemos el frame de la camara
    _, frame = cap.read()
    frame = cv2.resize(frame, (320,240))
    # Lo convertimos a RGBA
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
    # Lo pasamos a CUDA para que se puedea usar con la net
    frame = jetson.utils.cudaFromNumpy(frame)
    
    detections = net.Detect(frame, 320,240)
    print(f"detections: {detections}") 

    frame = jetson.utils.cudaToNumpy(frame, 320,240,4)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)
    
    cv2.imshow('detect', frame)


#--------------otro
    _, frame = cap2.read()
    frame = cv2.resize(frame, (240,320))
    # Lo convertimos a RGBA
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
    # Lo pasamos a CUDA para que se puedea usar con la net
    frame = jetson.utils.cudaFromNumpy(frame)
    
    detections = net.Detect(frame, 240,320)
    print(f"detections: {detections}") 

    frame = jetson.utils.cudaToNumpy(frame, 240,320,4)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)
    
    cv2.imshow('detect2', frame)
    
    _, frame = cap3.read()
    frame = cv2.resize(frame, (240,320))
    # Lo convertimos a RGBA
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
    # Lo pasamos a CUDA para que se puedea usar con la net
    frame = jetson.utils.cudaFromNumpy(frame)
    
    detections = net.Detect(frame, 240,320)
    print(f"detections: {detections}") 

    frame = jetson.utils.cudaToNumpy(frame, 240,320,4)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)
    
    cv2.imshow('detect3', frame)



    if cv2.waitKey(16) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
