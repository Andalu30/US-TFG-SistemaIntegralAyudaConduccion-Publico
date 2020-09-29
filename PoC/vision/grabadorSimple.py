import os
import cv2
import sys
import time
import numpy as np
from threadedCVaukey import inputDatosVision


grabar = sys.argv[1].lower() == 'true'
carpeta = sys.argv[2]

if grabar:

    if not os.path.exists(f"archivosVideo/conAukey/{carpeta}"):
        os.makedirs(f"archivosVideo/conAukey/{carpeta}")

    # Video writers
    writer_main = cv2.VideoWriter(f"archivosVideo/conAukey/{carpeta}/main.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30 ,(1920,1080))


cap = cv2.VideoCapture(4, cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


while True:
    _, frame1 = cap.read()

    #Volteado horizontal para el montaje de la camara del revés.
    frame1 = cv2.flip(frame1, 0)
    frame1 = cv2.flip(frame1, 1) 
    # Grabador
    if grabar:
        writer_main.write(frame1)

    # GUI
    main_gui = cv2.resize(frame1, (1280,720))
    cv2.imshow('Camera previsualization', main_gui)


    #WaitKey 33 para grabar a 30 fps
    if chr(cv2.waitKey(33)&255) == 'q':
        break


if grabar:
    writer_main.release()

cv2.destroyAllWindows()
cap.release()
