import time
import cv2
import numpy as np
from threadedCV import inputDatosVision


visionData = inputDatosVision(2,3,openniStream='RGB')

while True:
    [frame1, frame2, depth, opennistream] = visionData.read()
        
    # Cambia el tipo de el depthmap
    depth = depth.astype('float32')
    depth = cv2.cvtColor(depth, cv2.COLOR_GRAY2BGR)

    # Y del infrarrojo si se esta usando
    if visionData.getTipoStream() == 'IR':
        opennistream = opennistream.astype('float32')
        opennistream = cv2.cvtColor(opennistream, cv2.COLOR_GRAY2BGR)


    # gui
    top = np.hstack((depth, opennistream))
    bottom = np.hstack((frame1,frame2))

    gui = np.vstack((top,bottom))
    #cv2.imshow('GUI', gui)
    
    cv2.imshow('test1', top)
    cv2.imshow('test2', bottom)
    cv2.imshow('main', opennistream)

    if chr(cv2.waitKey(16)&255) == 'q':
        break

visionData.desconectarDatosVision()