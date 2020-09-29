import jetson.inference
import jetson.utils

import cv2
import numpy as np


# Cargamos el model de deteccion
net = jetson.inference.detectNet("ssd-inception-v2", threshold=0.4)

netseg = jetson.inference.segNet("fcn-resnet18-cityscapes-2048x1024")


cap = cv2.VideoCapture("../videos/calles13/main.avi")
# cap2 = cv2.VideoCapture("../videos/side1.avi")
# cap3 = cv2.VideoCapture("../videos/side2.avi")

while True:
	# Recojemos el frame de la camara
    _, frame = cap.read()
    frameorig = frame
    
    #frame = cv2.resize(frame, (640,480))
    # Lo convertimos a RGBA
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

    # Lo pasamos a CUDA para que se puedea usar con la net
    frame = jetson.utils.cudaFromNumpy(frame)
    
    detections = net.Detect(frame, 1920,1080)
    print(f"detections: {detections}") 

    frame = jetson.utils.cudaToNumpy(frame, 1920,1080,4)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)
    
    cv2.putText(frame, f"FPS: {net.GetNetworkFPS()}", (25,25), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

    frame_gui = cv2.resize(frame, (1280,720))
    cv2.imshow('detect', frame_gui)



# #--------------otro
#     _, frame = cap2.read()
#     frame = cv2.resize(frame, (240,320))
#     # Lo convertimos a RGBA
#     frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
#     # Lo pasamos a CUDA para que se puedea usar con la net
#     frame = jetson.utils.cudaFromNumpy(frame)
    
#     detections = net.Detect(frame, 240,320)
#     print(f"detections: {detections}") 

#     frame = jetson.utils.cudaToNumpy(frame, 240,320,4)
#     frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)
    
#     cv2.imshow('detect2', frame)
    
#     _, frame = cap3.read()
#     frame = cv2.resize(frame, (240,320))
#     # Lo convertimos a RGBA
#     frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
#     # Lo pasamos a CUDA para que se puedea usar con la net
#     frame = jetson.utils.cudaFromNumpy(frame)
    
#     detections = net.Detect(frame, 240,320)
#     print(f"detections: {detections}") 

#     frame = jetson.utils.cudaToNumpy(frame, 240,320,4)
#     frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)
    
#     cv2.imshow('detect3', frame)


#     print(f"Object FPS: {net.GetNetworkFPS()}")


#segmentation---------------------------------

    frameorig = cv2.resize(frameorig, (1024,720)) #Porque cojones soy tan estupìdo??
    
    frameorig = cv2.cvtColor(frameorig, cv2.COLOR_RGB2RGBA)
    frameorig = jetson.utils.cudaFromNumpy(frameorig)
    
    #netseg.SetOverlayAlpha(0.9)
    netseg.Process(frameorig, 1024, 720)
    #netseg.Overlay(frameorig,640,480)
    netseg.Mask(frameorig, 1024, 720)

    frameorig = jetson.utils.cudaToNumpy(frameorig, 1024, 720, 4)
    frameorig = cv2.cvtColor(frameorig, cv2.COLOR_RGBA2RGB).astype(np.uint8)

    print(netseg.GetNetworkFPS())

    #cv2.putText(frameorig, f"{netseg.GetNetworkFPS()}", (50,50), cv2.FONT_HERSHEY_COMPLEX,1,255)

    cv2.putText(frameorig, f"FPS: {netseg.GetNetworkFPS()}", (25,25), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

    segment_gui = cv2.resize(frameorig, (640,320))
    cv2.imshow('segment', segment_gui)



    if cv2.waitKey(16) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()