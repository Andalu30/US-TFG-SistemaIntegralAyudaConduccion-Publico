import time
import cv2
import numpy as np
import sys
import os
import random
import tensorflow as tf
import tensorrt as trt

sys.path.append('../usoDeDatos')
from ClaseObjetosDetectadosPredict import Vehiculo, Peaton, algoritmoTrackingVehiculos

sys.path.append('../vision')
from threadedCVsimulmain import inputDatosVision
from ClaseModelosIAFull import objectDetectionJetsonInference, segmentationJetsonInference



# Funciones de ayuda
def esVehiculo(num):
    return (num in [2, 3, 4, 6, 8])

def esSemaforo(n):
    return n is 10

def esStop(n):
    return n is 13



# Inicialización
visionData = inputDatosVision('../videos/calles9')
detectorObjetos = objectDetectionJetsonInference(threshold=0.6)
segmentadorCamara = segmentationJetsonInference(modelo='fcn-resnet18-cityscapes-2048x1024')
semafModel = tf.keras.models.load_model('binario10TRT')


#semaforos
semaforo_generico = cv2.imread('../usoDeDatos/semaforo_generico.jpg')
semaforo_rojo = cv2.imread('../usoDeDatos/semaforo_rojo.jpg')
semaforo_ambar = cv2.imread('../usoDeDatos/semaforo_ambar.jpg')
semaforo_verde = cv2.imread('../usoDeDatos/semaforo_verde.jpg')
semaforo = False

#stops
imgSTOP = cv2.imread('../usoDeDatos/stop.png')
framesSinStop = 0

#track vehiculos
vehiculosFrameAnterior = []





while True:

# Input de datos
    # Cámaras
    (main, side1, side2) = visionData.read()



    cuadros = main


# Modelos IA
    # Object Detection
    objs1, outdetec1 = detectorObjetos.deteccionRGBframe(main)

    # Semantic Segmentation
    seg1 = segmentadorCamara.segmentRGBframe(main)

    # Classification general


# Uso de los datos
    
    # Analisis Semáforos
    semaforo = None

    semaforos = list(filter(lambda x: esSemaforo(x.ClassID), objs1))
    for i in semaforos:
        objs1.remove(i)


    data = np.ndarray(shape=(1, 100, 100, 3), dtype=np.float32)

    for obj in semaforos:
        crop_semaforo = main[int(obj.Top):int(obj.Bottom), int(obj.Left):int(obj.Right)]
        test_img = cv2.resize(crop_semaforo, (100, 100))
        #test_img = np.expand_dims(test_img, axis=0)
        #test_img = tf.cast(test_img, tf.float32)

        data[0] = test_img
        prediccionSemaforo = semafModel.predict(data)
        print(f'prediccionSemaforo -> {prediccionSemaforo}')
        
        if abs(prediccionSemaforo[0][0]-prediccionSemaforo[0][1]) < 0.85:
            semaforo = 'undef'
        elif np.argmax(prediccionSemaforo[0]) == 0:
            semaforo = 'red'
            guiSTOP = True
            framesSinStop = 0
        elif np.argmax(prediccionSemaforo[0]) == 1:
            semaforo = 'green'

        start_point = (int(obj.Left), int(obj.Top))
        end_point = (int(obj.Right), int(obj.Bottom))

        cuadros = cv2.rectangle(cuadros, start_point, end_point, (255, 0, 0), 3)

        cuadros = cv2.putText(cuadros, f'{obj.ClassID} {obj.ClassID} {obj.Confidence:.2f}% ID:{obj.Instance}',
                            start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        break



    # Señales
    senyalSTOP = list(filter(lambda x: esStop(x.ClassID), objs1))
    #for i in senyalSTOP:
        #objs1.remove(i)

    if len(senyalSTOP) != 0:
        guiSTOP = True
        framesSinStop = 0
    else:
        framesSinStop +=1
        if framesSinStop > 5:
            guiSTOP = False
        else:
            guiSTOP = True



    # Track y prediccion vehículos
    vehiculos = []
    for oj in objs1:
        if esVehiculo(oj.ClassID):
            v = Vehiculo(oj, random.randrange(10,100))
            vehiculos.append(v)

    vehiculosTrackeados = []

    if vehiculosFrameAnterior == []:
        vehiculosFrameAnterior = vehiculos
    else:
        vehiculosTrackeados = algoritmoTrackingVehiculos(vehiculosFrameAnterior, vehiculos, limiteDistancia=200)
        vehiculosFrameAnterior = vehiculosTrackeados





    # Track y prediccion peatones



# Toma de decisiones


# Notificaciones y GUI
    # Pantalla
        # OpenCV
            # Camaras
    #cv2.imshow('Canara main', main)
    #cv2.imshow('Camara side1', side1)
    #cv2.imshow('Camara side2', side2)

            # Object Detection
    #cv2.imshow('Detect main',  outdetec1)
    #cv2.imshow('Detect side1', outdetec2)
    #cv2.imshow('Detect side2', outdetec3)

            # Segmentation
    seg_gui = cv2.resize(seg1, (320,180))
    cuadros[ 900:1080, 1600:1920] = seg_gui
    #cv2.imshow('seg', seg_gui)
    #cv2.imshow('Segmentation main', seg1)
    #cv2.imshow('Segmentation main', seg2)
    #cv2.imshow('Segmentation main', seg3)

    #STOP
    if guiSTOP:
        stop_200 = cv2.resize(imgSTOP, (200, 200))
        cuadros[700:900, 1720:1920] = stop_200

    #Semaforos
    if semaforo is 'red':
        rojo_100 = cv2.resize(semaforo_rojo, (100,200))
        cuadros[700:900, 1620:1720] = rojo_100
    elif semaforo is 'green':
        verde_100 = cv2.resize(semaforo_verde, (100, 200))
        cuadros[700:900, 1620:1720] = verde_100


    #Vehiculos
    for obj in vehiculosTrackeados:
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
        
        cuadros = cv2.putText(cuadros, f'PREDICT - ID:{obj.getID()}', predict_start,
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA) # Texto prediccion

        cuadros = cv2.putText(cuadros, f'{obj.getID()}',
                                centro, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1, cv2.LINE_AA)


    cuadros = cv2.resize(cuadros, (1280,720))
    cv2.imshow('Output',  cuadros)

    if chr(cv2.waitKey(16)&255) == 'q':
        break


visionData.desconectarDatosVision()
cv2.destroyAllWindows()
