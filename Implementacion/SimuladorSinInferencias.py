import time
import cv2
import numpy as np
import logging
import multiprocessing
import random
from playsound import playsound
import tensorflow as tf
import imutils
import os


from RecolectorDatos import connectCARLAsimple, connectCARLAcompleto, driverAttention
#from ModelosIA import objectDetectionJetsonInference, segmentationJetsonInference, clasificacionSemaforos
from ModelosIA import deteccionInterseccion, RoadDirector

from ClasesAuxiliares import Semaforo
#from AlgoritmosTracking import algoritmoTrackingVehiculos
from UsoDatos import VistaTopDown, marcasCalzada
from FuncionesAuxiliares import *
from Gui import InterfazGrafica, notificacionesSonido, pantallaCarga

gui = InterfazGrafica()
sonidos = notificacionesSonido()


conectorConCarla = connectCARLAcompleto('192.168.0.17', 'tesla.model3')
#detectorObjetos = objectDetectionJetsonInference(threshold=0.1)
#segmentadorCamara = segmentationJetsonInference(modelo='fcn-resnet18-cityscapes-1024x512')
#algTrackVehiculos = algoritmoTrackingVehiculos()
#vehiculosTrackeados = []


#analisisSemaf = clasificacionSemaforos('Binario10epochsOptimizado')

roadDirector = RoadDirector(modelo='RoadDirector-test1722')

analisisInterseccion = deteccionInterseccion(modelo='InterseccionesConv2d91%')
ModulomarcasCalzada = marcasCalzada()


moduloTopDown = VistaTopDown()
driverAttention = driverAttention()



while True:
    start_time = time.time()  # Time inicial del bucle para calcular FPS

    # Input de datos
    # Cámaras
    main, lat1, lat2 = conectorConCarla.getDatosVision()

    main = procesaImgCarla(main)
    lat1 = procesaImgCarlaPeq(lat1)
    lat2 = procesaImgCarlaPeq(lat2)

    cv2.imshow('main',main)


    # Sensores ODB
    velocidad = conectorConCarla.getVelocidad()
    
    acelerador = conectorConCarla.getAcelerador()
    freno = conectorConCarla.getFreno()
    anguloVolante = conectorConCarla.getVolante()
    limiteVelocidad = conectorConCarla.getLimiteVelocidad()

    # Tobii Driver Attention
    atencion_conductor = driverAttention.getDriverAttention()
    sin_atencion = driverAttention.getTimerAttention()

    notificaConductorSinAtencion = False
    if sin_atencion > 1.5:
        notificaConductorSinAtencion = True
        sonidos.reproduceAlertaQuindarStart()
        sonidos.reproduceAlertaQuindarEnd()

    

# Modelos IA

    #Object Detection
    #objs1, outdetec1, fpsDet1 = detectorObjetos.deteccionRGBframe640(main)
    #objs2, outdetec2, fpsDet2 = detectorObjetos.deteccionRGBframe320(lat1)
    #objs3, outdetec3, fpsDet3 = detectorObjetos.deteccionRGBframe320(lat2)
    #outdetec2 = np.zeros((320, 240, 3))
    #outdetec3 = np.zeros((320, 240, 3))

    #cv2.imshow('Main', main)
    #cv2.imshow('lat1', lat1)
    #cv2.imshow('lat2', lat2)

    #cv2.imshow("outdetect", outdetec1)
    #cv2.imshow("outdetect1", outdetec2)
    #cv2.imshow("outdetect2", outdetec3)

    # Semantic Segmentation
    #seg1, fpsSeg1 = segmentadorCamara.segmentRGBframe640(main)
    fpsSeg1 = 0.0
    #cv2.imshow("segment", seg1)

    # Classification general


# Uso de los datos
    # Vista top-down 360º
    moduloTopDown.computaVistaTopDown(main, lat1, lat2)
    topDown = moduloTopDown.getVistaTopDown()

    # Segmentación
    # moduloTopDown.computaVistaTopDown(seg1, lat1, lat2)
    # topDown2 = moduloTopDown.getVistaTopDown()

    # Lineas/carriles
    topDownMasked = moduloTopDown.getVistaTopDownEditada()

    # Señales

    # Analisis Semáforos
    # semaforos = getSemaforos(objs1)
    # fps_semafs = 0.0

    # if semaforos:

    #     semaforos.sort(key=lambda x: x.getLeft_nv())
    #     semaforosBusqPrincipal = semaforos.copy()

    #     semaforosBusqPrincipal.sort(key=lambda x: abs(x.getLeft_nv() - 320))
    #     semaforoPrincipal = semaforosBusqPrincipal[0]

    #     top = int(semaforoPrincipal.getTop_nv())
    #     bot = int(semaforoPrincipal.getBottom_nv())
    #     rig = int(semaforoPrincipal.getRight_nv())
    #     lef = int(semaforoPrincipal.getLeft_nv())

    #     # Controlamos que al introducir el padding no nos salgamos de la imagen.
    #     padding = 5
    #     if top < padding or bot > 480-padding or rig > 640-padding or lef < padding:
    #         padding = 0
    #     rgb_semafPrin = main[top-padding:bot+padding, lef-padding:rig+padding]

    #     analisisSemaf.clasificaSemaforo(rgb_semafPrin)

        # semaforosgui = np.zeros((100, 600, 3), np.uint8)
        # for i,semaf in enumerate(semaforos):
        #     top = int(semaf.getTop_nv())
        #     bot = int(semaf.getBottom_nv())
        #     rig = int(semaf.getRight_nv())
        #     lef = int(semaf.getLeft_nv())
        #     # Controlamos que al introducir el padding no nos salgamos de la imagen.
        #     padding = 5
        #     if top < padding or bot > 480-padding or rig > 640-padding or lef <padding:
        #         padding = 0
        #     rgb = main[top-padding:bot+padding , lef-padding:rig+padding]
        #     rgb = cv2.resize(rgb, (100, 100)) #El resize ya no deberia de dar problemas porque no llegariamos con img vacias.
        #     if semaf == semaforoPrincipal:
        #         rgb = cv2.putText(rgb, 'Principal', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        #         semafrgbqt = rgb
        #     else:
        #         izq = semaf.getLeft_nv()
        #         rgb = cv2.putText(rgb, f'{izq}', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        #     semaforosgui[0:100, i*100:i*100+100, :] = rgb
        # cv2.imshow('semaforos', semaforosgui)
    #else:
    #    analisisSemaf.noHaySemaforo()

    #semaforo = analisisSemaf.getStatusSemaforo()
    #fps_semafs = analisisSemaf.getSemafFPS()
    semaforo = None

    #cv2.imshow('frontMaskedFunc', moduloTopDown.getFrontMasked())
    
    frontmasked = moduloTopDown.getFrontMasked()
    #cv2.imshow('Front masked', frontmasked)



    #Interseccion
    analisisInterseccion.analisisDeInterseccion(frontmasked)
    interseccion = analisisInterseccion.getPrediccionInterseccion()
    fps_interseccion = analisisInterseccion.getFPS()

    #Marcas calzada
    inmediatamenteDelante = moduloTopDown.getInmediatamentedelante()
    ModulomarcasCalzada.analisisMarcasCalzada(inmediatamenteDelante)
    calzada = ModulomarcasCalzada.getMarcasCalzada()

    pasoPeatones = calzada['cebra']
    senyalStop = calzada['stop']


    #RD
    #cv2.imshow('0oagaogias', inmediatamenteDelante)
    roadDirector.analisisRD(inmediatamenteDelante)
    rd_wheel = roadDirector.getRDwheelNomalized()
    # #print(f'RD {rd_wheel}', anguloVolante)
    # print(roadDirector.getRDwheelNomalized())

    # anguloSobre90_predict = -(roadDirector.getRDwheelNomalized()*90)/0.7
    # anguloSobre90_real = -(anguloVolante*90)/0.7



    # wheelimg = cv2.resize(cv2.imread('resources/guiImg/wheel.png'), (100, 100))
    # wheelimg_pred = imutils.rotate(wheelimg, anguloSobre90_predict)
    # wheelimg_real = imutils.rotate(wheelimg, anguloSobre90_real)

    # cv2.imshow('Wheel predict', wheelimg_pred)
    # cv2.imshow('Wheel real', wheelimg_real)




# Toma de decisiones


# Notificaciones y GUI
    # Sonido

    # Pantalla
    # Qt
    fps_vision = 1 / (time.time() - start_time)



                 #mainCam, lat1, lat2, velocidad, atencion_conductor, fps_vision, topdown, topDownMasked, semaforo, fps_detect, fps_semafs, num_semafs, interseccion, fps_interseccion, pasoPeatones, existeStop, acelerador, freno, anguloVolante, anguloVolante_predict, notificaConductorSinAtencion, notificaCambioSemaforoVerde, limiteVelocidad, porEncimalimiteVel, senyalizquierda, senyalderecha, senyaldelanteDer, senyaldelanteIzq = datos
    datosParaQT = [main, lat1, lat2, velocidad, atencion_conductor, fps_vision, topDown, topDownMasked, semaforo,  0.0,             0.0,       0,        interseccion, fps_interseccion, pasoPeatones, senyalStop, acelerador, freno, anguloVolante, rd_wheel, notificaConductorSinAtencion, False, limiteVelocidad, False, False, False, False, False]
    
    gui.actualizaInfoGui(datosParaQT)


    #Recordatorio para bucle OpenCV
    cv2.imshow('Recordatorio Aplicación', gui.getImgBucleCV())

    #Break del loop de OpenCV
    if chr(cv2.waitKey(1) & 255) == 'q':
        break

#---------------------------------------------

sonidos.reproduceAlertaQuindarEnd()

# Cerramos GUI
gui.cierraGui()

# Desconectamos los sensores
conectorConCarla.desconectarDatosVision()
driverAttention.desconecta()

# Jetson Inference se desconecta automaticamente.
# Cerramos ventanas de OpenCV
cv2.destroyAllWindows()



# print('Reproduciendo sonido de warning')
# playsound('resources/quindarTones/end.ogg')

print('Adios!')
