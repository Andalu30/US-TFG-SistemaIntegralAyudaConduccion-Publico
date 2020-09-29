import time
import cv2
import numpy as np
import sys 
import copy
import random

sys.path.append('../vision')

from threadedCVsimul import inputDatosVision
from ClaseModelosIA import objectDetectionJetsonInference


def esVehiculo(num):
    return (num in [2, 3, 4, 6, 8])

def esSemaforo(n):
    return n is 10


# Inicialización
visionData = inputDatosVision('../videos/4')
detectorObjetos = objectDetectionJetsonInference(threshold=0.2)

deteccionesFrameAnterior = [] 

semaforo_generico = cv2.imread('semaforo_generico.jpg')
semaforo_rojo = cv2.imread('semaforo_rojo.jpg')
semaforo_ambar = cv2.imread('semaforo_ambar.jpg')
semaforo_verde = cv2.imread('semaforo_verde.jpg')

semaforo = False



while True:

# Input de datos
    # Cámaras
    (main, side1, side2) = visionData.read()


# Modelos IA
    # Object Detection
    objs1, outdetec1 = detectorObjetos.deteccionRGBframe(main)






    # Tracking vehiculos nuevos:

    def algoritmoTrackingVehiculos(actual, frameAnterior, limiteDistancia):

        def detecAnteriorMasCerca(det, lista):
            #Centro
            (x,y) = det.Center
            centro = np.array((int(x),int(y)))
            
            centrosAnteriores = []
            for i in lista:
                (x, y) = i.Center
                anterior = (int(x), int(y))
                centrosAnteriores.append(anterior)

            distancias = []

            for i in centrosAnteriores:
                c = np.array(i)
                dist = np.linalg.norm(centro-c)
                distancias.append(dist)

            distancia = np.min(distancias)
            mas_cerca = frameAnterior[np.argmin(distancias)]

            print(f'distancia -> {distancia}')

            return mas_cerca, distancia


        res = []
        #Filtros vehiculos
        frameAnterior = list(filter(lambda x: esVehiculo(x.ClassID), frameAnterior))
        actual = list(filter(lambda x: esVehiculo(x.ClassID), actual))

        # Bucle (usamos instance como ID)
        for det in actual:
            masCerca, distancia = detecAnteriorMasCerca(det, frameAnterior)
        
            if distancia > limiteDistancia:
                ids = map(lambda x: x.Instance, frameAnterior)
                idnuevo = random.choice([x for x in range(max(ids)+1) if x not in ids])
                det.__setattr__('Instance', idnuevo)
                
                actual.remove(det)
                res.append(det)
            else:
                det.__setattr__('Instance', masCerca.Instance)
                frameAnterior.remove(masCerca)
                actual.remove(det)
                res.append(det)
        
        return res


    # seccion
    deteccionesActuales = objs1
    
    if deteccionesFrameAnterior == []:
        if objs1 == []:
            deteccionesFrameAnterior == []
        else:
            deteccionesFrameAnterior = objs1

        distanciaMax = 50
        deteccionesActualizadas = algoritmoTrackingVehiculos(deteccionesFrameAnterior, deteccionesActuales, distanciaMax)

        objs1 = deteccionesActualizadas
        
    
# Notificaciones y GUI
    # Object detection personal
    cuadros = main
    for obj in objs1:
        if esVehiculo(obj.ClassID):
            # crop = main[int(obj.Top):int(obj.Bottom), int(obj.Left):int(obj.Right)]
            # cv2.imshow(f'{obj.Instance} - Tracking', crop)
            start_point = (int(obj.Left), int(obj.Top))
            end_point = (int(obj.Right), int(obj.Bottom))

            (x, y) = obj.Center
            centro = (int(x), int(y))
            
            cuadros = cv2.rectangle(cuadros, start_point, end_point, (0,255,255), 1)
            cuadros = cv2.putText(cuadros, f'{f"V({obj.ClassID})" if esVehiculo(obj.ClassID) else f"{obj.ClassID}"} {obj.Confidence:.2f}% ID:{obj.Instance}',
                                  start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1, cv2.LINE_AA)

            cuadros = cv2.putText(cuadros, f'{obj.Instance}',
                                  centro, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # else:

        #     if esSemaforo(obj.ClassID) and obj.Confidence > 0.60:
        #         semaforo = True
        #         crop_semaforo = main[int(obj.Top):int(obj.Bottom), int(obj.Left):int(obj.Right)]
        #         cv2.imshow(f'crop_semaforo', crop_semaforo)
        #     else:
        #         semaforo = False


        #     start_point = (int(obj.Left), int(obj.Top))
        #     end_point = (int(obj.Right), int(obj.Bottom))

        #     (x, y) = obj.Center
        #     centro = (int(x), int(y))

        #     cuadros = cv2.rectangle(
        #         cuadros, start_point, end_point, (255, 255, 255), 1)
        #     cuadros = cv2.putText(cuadros, f'{obj.ClassID} {obj.ClassID} {obj.Confidence:.2f}% ID:{obj.Instance}',
        #                           start_point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)

        #     cuadros = cv2.putText(cuadros, f'{obj.Instance}',
        #                           centro, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('cuadros', cuadros)


    imsemaforo = cv2.imread('semaforo.jpg')
    if semaforo is True:
        cv2.imshow('semaforo', semaforo_generico)
    else:
        try:
            cv2.destroyWindow('semaforo')
            cv2.destroyWindow('crop_semaforo')
            
        except:
            pass




        # Object Detection
    cv2.imshow('Detect main',  outdetec1)

 
    if chr(cv2.waitKey(16)&255) == 'q':
        break


visionData.desconectarDatosVision()
cv2.destroyAllWindows()
