import time
import cv2
import numpy as np

from threadedCVsimul import inputDatosVision
from ClaseModelosIA import objectDetectionJetsonInference, segmentationJetsonInference


# Inicialización
visionData = inputDatosVision('../videos/4')
detectorObjetos = objectDetectionJetsonInference(threshold=0.4)
segmentadorCamara = segmentationJetsonInference(modelo='fcn-resnet18-cityscapes-1024x512')

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
    # objs2, outdetec2 = detectorObjetos.deteccionRGBframe(side1)
    # objs3, outdetec3 = detectorObjetos.deteccionRGBframe(side2)

    # Semantic Segmentation
    seg1 = segmentadorCamara.segmentRGBframe(main)
    #seg2 = segmentadorCamara.segmentRGBframe(side1)
    #seg3 = segmentadorCamara.segmentRGBframe(side2)

    # Classification general


# Uso de los datos
    # Vista top-down 360º
        # Camaras

        # Segmentación
    
    
    # Lineas/carriles

    # Señales

    # Analisis Semáforos

    # Track y prediccion (kalman) vehículos

    # Track y prediccion (kalman) peatones


# Toma de decisiones


# Notificaciones y GUI
    # Sonido



    # Pantalla
        # OpenCV
            # Camaras
    #cv2.imshow('Canara main', main)
    #cv2.imshow('Camara side1', side1)
    #cv2.imshow('Camara side2', side2)

            # Object Detection
    cv2.imshow('Detect main',  outdetec1)
    #cv2.imshow('Detect side1', outdetec2)
    #cv2.imshow('Detect side2', outdetec3)

            # Segmentation
    cv2.imshow('Segmentation main', seg1)
    #cv2.imshow('Segmentation main', seg2)
    #cv2.imshow('Segmentation main', seg3)

        # Qt?



    if chr(cv2.waitKey(16)&255) == 'q':
        break

visionData.desconectarDatosVision()
cv2.destroyAllWindows()
