import time
import cv2
import numpy as np
import sys 
import copy
import random


from ClaseObjetosDetectadosPredict import Vehiculo, Peaton, algoritmoTrackingVehiculos
sys.path.append('../vision')
from threadedCVsimulmain import inputDatosVision
from ClaseModelosIAFull import objectDetectionJetsonInference


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
    #cuadros = main
    cuadros = np.zeros_like(main)
    for obj in vehiculosTrackeados:
        if obj.Confidence is not 0:
            #crop = main[int(obj.Top):int(obj.Bottom), int(obj.Left):int(obj.Right)]
            #crop = cv2.resize(crop, (250,250))
            #cuadros[ 0: 250 , 1000:1250] = crop
            #cv2.imshow(f'{obj.Instance} - Tracking', crop)
            
            start_point = (int(obj.getLeft_nv()), int(obj.getTop_nv()))
            end_point = (int(obj.getRight_nv()), int(obj.getBottom_nv()))

            aux2 = (int(obj.getRight_nv()), int(obj.getTop_nv()))
            aux3 = (int(obj.getLeft_nv()), int(obj.getBottom_nv()))

            centro = obj.getCentro()
            
            # pred -> Top Bot L R
            predict_start = (obj.getPrediccion()[2], obj.getPrediccion()[0])
            predict_end = (obj.getPrediccion()[3], obj.getPrediccion()[1])

            aux2_p = (int(obj.getPrediccion()[3]), int(obj.getPrediccion()[0]))
            aux3_p = (int(obj.getPrediccion()[2]), int(obj.getPrediccion()[1]))
            
            
            cuadros = cv2.line(cuadros, start_point, predict_start, (255,255,255), 1)
            cuadros = cv2.line(cuadros, end_point, predict_end, (255,255,255), 1)
            cuadros = cv2.line(cuadros, aux2, aux2_p, (255,255,255), 1)
            cuadros = cv2.line(cuadros, aux3, aux3_p, (255,255,255), 1)

            
            
            cuadros = cv2.rectangle(cuadros, start_point, end_point, (0,0,255), 1) # Real
            cuadros = cv2.rectangle(cuadros, predict_start, predict_end, (0,255,0), 1) # Prediccion

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
