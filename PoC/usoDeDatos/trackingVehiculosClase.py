import time
import cv2
import numpy as np
import sys 
import copy

sys.path.append('../vision')

from threadedCVsimulmain import inputDatosVision
from ClaseModelosIAFull import objectDetectionJetsonInference
from ClaseObjetosDetectados import Vehiculo, Peaton, algoritmoTrackingVehiculos


# Inicialización
visionData = inputDatosVision('../videos/calles21')
detectorObjetos = objectDetectionJetsonInference(threshold=0.6)

vehiculosFrameAnterior = []



def esVehiculo(obj):
    return (obj.ClassID in [2,3,4,6,8])
    



while True:

    time_inicio = time.time()

# Input de datos
    # Cámaras
    (main,side1,side2) = visionData.read()


# Modelos IA
    # Object Detection
    objs1, outdetec1 = detectorObjetos.deteccionRGBframe(main)

    import random

    # Filtramos por vehículos y convertimos en nuestra clase
    vehiculos = []
    for loopID, oj in enumerate(objs1):
        if esVehiculo(oj):
            v = Vehiculo(oj, random.randrange(10,100))
            vehiculos.append(v)


    vehiculosTrackeados = []

    if vehiculosFrameAnterior == []:
        vehiculosFrameAnterior = vehiculos
        #continue        
    else:
        vehiculosTrackeados = algoritmoTrackingVehiculos(vehiculosFrameAnterior, vehiculos, limiteDistancia=200)
        vehiculosFrameAnterior = vehiculosTrackeados





    print(f'num vehiculos: {len(vehiculosTrackeados)}')









        
    











# GUI
    cuadros = main
    for obj in vehiculosTrackeados:
        # crop = main[int(obj.Top):int(obj.Bottom), int(obj.Left):int(obj.Right)]
        # cv2.imshow(f'{obj.Instance} - Tracking', crop)
        start_point = (int(obj.getLeft_nv()), int(obj.getTop_nv()))
        end_point = (int(obj.getRight_nv()), int(obj.getBottom_nv()))
        
        centro = obj.getCentro()
        
        cuadros = cv2.rectangle(cuadros, start_point, end_point, (0,0,255), 1)
        cuadros = cv2.putText(cuadros, f'V({obj.getClassID_nv()}) {obj.getConfidence_nv():.2f}% ID:{obj.getID()}',
                                start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)

        cuadros = cv2.putText(cuadros, f'{obj.getID()}',
                                centro, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1, cv2.LINE_AA)



    cuadros = cv2.resize(cuadros, (1280,720))
    cv2.imshow('cuadros', cuadros)





        # Object Detection
    #cv2.imshow('Detect main',  outdetec1)

 
    time_fin = time.time()
    elapsed = time_fin - time_inicio
    fps = 1/elapsed
    print(f'FPS completo: {fps}')

    if chr(cv2.waitKey(1)&255) == 'q':
        break


visionData.desconectarDatosVision()
cv2.destroyAllWindows()
