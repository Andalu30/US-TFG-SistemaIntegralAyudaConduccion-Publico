import os
import cv2
import sys
import time
import numpy as np
from threadedCVaukey import inputDatosVision



grabar = sys.argv[1].lower() == 'true'
carpeta = sys.argv[2]

if grabar:

    if not os.path.exists(f"archivosVideo/{carpeta}"):
        os.makedirs(f"archivosVideo/{carpeta}")

    # Video writers
    writer_main = cv2.VideoWriter(f"archivosVideo/{carpeta}/main.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(1920,1080))
    writer_side1 = cv2.VideoWriter(f"archivosVideo/{carpeta}/side1.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(480,640))
    writer_side2 = cv2.VideoWriter(f"archivosVideo/{carpeta}/side2.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(480,640))

visionData = inputDatosVision(2,3,4)

while True:
    (frame1, frame2, frame3) = visionData.read()
        
    frame2 = cv2.rotate(frame1, cv2.ROTATE_90_COUNTERCLOCKWISE)
    frame3 = cv2.rotate(frame2, cv2.ROTATE_90_CLOCKWISE)

    # Grabador
    if grabar:
        writer_main.write(frame1)
        writer_side1.write(frame2)
        writer_side2.write(frame3)

    # GUI
    sides = np.hstack((frame2,frame3))

    main_gui = cv2.resize(frame1, (640,480))
    cv2.imshow('main', main_gui)
    cv2.imshow('sides', sides)



    if chr(cv2.waitKey(16)&255) == 'q':
        break


if grabar:
    writer_main.release()
    writer_side1.release()
    writer_side2.release()

cv2.destroyAllWindows()
visionData.desconectarDatosVision()