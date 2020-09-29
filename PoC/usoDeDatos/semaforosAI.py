import time
import cv2
import numpy as np
import sys 
import copy
import random
import time

import tensorflow as tf

sys.path.append('../vision')

from threadedCVsimulmain import inputDatosVision
from ClaseModelosIAFull import objectDetectionJetsonInference



def esVehiculo(num):
    return (num in [2, 3, 4, 6, 8])


def esSemaforo(n):
    return n is 10

def esStop(n):
    return n is 13


# Inicialización

semafModel = tf.keras.models.load_model('nuevoModeloBinario10epochs.h5')


visionData = inputDatosVision('../videos/calles21')
detectorObjetos = objectDetectionJetsonInference(threshold=0.1)

semaforo_generico = cv2.imread('semaforo_generico.jpg')
semaforo_rojo = cv2.imread('semaforo_rojo.jpg')
semaforo_ambar = cv2.imread('semaforo_ambar.jpg')
semaforo_verde = cv2.imread('semaforo_verde.jpg')

imgSTOP = cv2.imread('stop.png')


semaforo = False

framesSinStop = 0





while True:

    inicio = time.time()

    # Input de datos
    # Cámaras
    (main, side1, side2) = visionData.read()


# Modelos IA
    # Object Detection
    objs1, outdetec1 = detectorObjetos.deteccionRGBframe(main)

    



    semaforos = list(filter(lambda x: esSemaforo(x.ClassID), objs1))
    for i in semaforos:
        objs1.remove(i)
    print(f'numero semaforos: {len(semaforos)}')


    senyalSTOP = list(filter(lambda x: esStop(x.ClassID), objs1))
    # for i in senyalSTOP:
    #     objs1.remove(i)
    print(f'numero STOP: {len(senyalSTOP)}')





    cuadros = main


    for obj in semaforos:
       
        borde = 0 # pixeles de borde por si
        crop_semaforo = main[int(obj.Top)-borde:int(obj.Bottom)+borde, int(obj.Left)-borde:int(obj.Right)+borde]

        test_img = cv2.resize(crop_semaforo, (100, 100))
        cuadros[0:100, 0:100] = test_img


        test_img = np.expand_dims(test_img, axis=0)
        test_img = tf.cast(test_img, tf.float32)

        pred_ini = time.time()
        prediccionSemaforo = semafModel.predict(test_img)
        print(
            f'prediccionSemaforo: {prediccionSemaforo} --> {np.argmax(prediccionSemaforo[0])} en {(time.time()-pred_ini)} ms')
        
        if abs(prediccionSemaforo[0][0]-prediccionSemaforo[0][1]) < 0.7:
            semaforo = 'undef'
        elif np.argmax(prediccionSemaforo[0]) == 0:
            semaforo = 'red'
        elif np.argmax(prediccionSemaforo[0]) == 1:
            semaforo = 'green'


        start_point = (int(obj.Left), int(obj.Top))
        end_point = (int(obj.Right), int(obj.Bottom))

        (x, y) = obj.Center
        centro = (int(x), int(y))

        cuadros = cv2.rectangle(cuadros, start_point, end_point, (255, 0, 0), 3)

        cuadros = cv2.putText(cuadros, f'{obj.ClassID} {obj.ClassID} {obj.Confidence:.2f}% ID:{obj.Instance}',
                            start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

        break

    if len(senyalSTOP) != 0:
        guiSTOP = True
        framesSinStop = 0
    else:
        framesSinStop +=1
        if framesSinStop > 5:
            guiSTOP = False
        else:
            guiSTOP = True


    for obj in objs1:
        start_point = (int(obj.Left), int(obj.Top))
        end_point = (int(obj.Right), int(obj.Bottom))

        (x, y) = obj.Center
        centro = (int(x), int(y))

        cuadros = cv2.rectangle(cuadros, start_point, end_point, (255, 255, 255), 1)

        cuadros = cv2.putText(cuadros, f'{obj.ClassID} {obj.ClassID} {obj.Confidence:.2f}% ID:{obj.Instance}',
                            start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        cuadros = cv2.putText(cuadros, f'{obj.Instance}',
                            centro, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)




    if guiSTOP:
        cuadros = cv2.putText(cuadros, f'STOP!!',
                              (100,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        stop_200 = cv2.resize(imgSTOP, (200, 200))
        cuadros[0:200, 100:300] = stop_200
        #cv2.imshow('STOP', imgSTOP)
    else:
        pass
        # try:
        #     cv2.destroyWindow('STOP')
        # except:
        #     pass

    if semaforo is 'undef':
        gen_100 = cv2.resize(semaforo_generico, (100, 100))
        cuadros[100:200, 0:100] = gen_100

    elif semaforo is 'red':
        cuadros = cv2.putText(cuadros, f'Semaforo - ROJO!!',
                              (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        rojo_100 = cv2.resize(semaforo_rojo, (100,100))
        cuadros[100:200, 0:100] = rojo_100

    elif semaforo is 'green':
        cuadros = cv2.putText(cuadros, f'Semaforo - VERDE',
                              (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        verde_100 = cv2.resize(semaforo_verde, (100, 100))
        cuadros[100:200, 0:100] = verde_100




    semaforo = None
    
        #cv2.imshow('semaforo', semaforo_verde)
    # else:
    #     try:
    #         cv2.destroyWindow('semaforo')
    #         #cv2.destroyWindow('crop_semaforo')

    #     except:
    #         pass

        # Object Detection
    #cv2.imshow('Detect main',  outdetec1)
    
    cuadros = cv2.resize(cuadros, (1280,720))
    cv2.imshow('cuadros', cuadros)


    print(f'FPS = {1/(time.time()-inicio)}')



    if chr(cv2.waitKey(16) & 255) == 'q':
        break


visionData.desconectarDatosVision()
cv2.destroyAllWindows()
