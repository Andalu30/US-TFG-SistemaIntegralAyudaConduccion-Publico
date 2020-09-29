import time
import cv2
import numpy as np

from vision/threadedCVsimul import inputDatosVision
from vison/ClaseObjectDetection import objectDetectionJetsonInference


# Inicialización
visionData = inputDatosVision('../videos/4')
detectorObjetos = objectDetectionJetsonInference(threshold=0.4)


while True:

# Input de datos
    # Cámaras
    (main, side1, side2) = visionData.read()

    # Sensores ODB

    # Sensores Arduino

    # Clasificación externa (Estado del conductor con una Raspberry? comunicación con sockets?)


# Modelos IA
    # Object Detection
    objs1, outdetec1 = detectorObjetos.deteccionRGBframe(main)
    objs2, outdetec2 = detectorObjetos.deteccionRGBframe(side1)
    objs3, outdetec3 = detectorObjetos.deteccionRGBframe(side2)

    # Semantic Segmentation


    # Classification general


# Uso de los datos
    # Vista top-down 360º
        # Camaras

        # Segmentación
    
    
    # Lineas/carriles

    # Señales

    # Semáforos

    # Track vehículos

    # Track peatones


# Toma de decisiones


# Notificaciones
    # Sonido


# GUI 
    # Camaras
    #cv2.imshow('Canara main', main)
    #cv2.imshow('Camara side1', side1)
    #cv2.imshow('Camara side2', side2)

    # Object Detection
    cv2.imshow('Detect main',  outdetec1)
    cv2.imshow('Detect side1', outdetec2)
    cv2.imshow('Detect side2', outdetec3)




    if chr(cv2.waitKey(16)&255) == 'q':
        break


visionData.desconectarDatosVision()
cv2.destroyAllWindows()
