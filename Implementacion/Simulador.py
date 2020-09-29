#---------------------------------------------#
#      Simulador.py - Conectado con Carla     #
#---------------------------------------------#


#---------------------------------------------#
#                   Imports                   #
#---------------------------------------------#
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
from ModelosIA import objectDetectionJetsonInference, segmentationJetsonInference, clasificacionSemaforos, deteccionInterseccion, RoadDirector
from ClasesAuxiliares import Semaforo
#from AlgoritmosTracking import algoritmoTrackingVehiculos
from ClaseObjetosDetectadosPredict import Vehiculo, Peaton, algoritmoTrackingVehiculos
from UsoDatos import VistaTopDown, marcasCalzada
from Gui import InterfazGrafica, OverlaysOpenCV, notificacionesSonido, pantallaCarga

from FuncionesAuxiliares import *


#---------------------------------------------#
#             Instanciacion de módulos        #
#---------------------------------------------#
gui = InterfazGrafica()
overlays = OverlaysOpenCV()
sonidos = notificacionesSonido()

conectorConCarla = connectCARLAcompleto('192.168.0.17', 'tesla.model3')
detectorObjetos = objectDetectionJetsonInference(threshold=0.0)

vehiculosFrameAnterior = []
peatonesFrameAnterior = []

roadDirector = RoadDirector(modelo='RoadDirector-test1722')

analisisSemaf = clasificacionSemaforos('ModeloKerasSemafConv2Dx25-3x3/_optimizadoTRT_FP16')
analisisInterseccion = deteccionInterseccion('InterseccionesConv2d91%/_optimizadoTRT_FP16')
ModulomarcasCalzada = marcasCalzada()

moduloTopDown = VistaTopDown()
driverAttention = driverAttention()

# Toma de decisiones
estadoAnteriorSemaf = None
notificacionSemaforoEnVerde = False


#---------------------------------------------#
#       Bucle Principal de la aplicacion      #
#---------------------------------------------#
while True:
    start_time = time.time()  # Time inicial del bucle para calcular FPS


    #----------------Obtencion de datos---------------#
    # Cámaras
    main, lat1, lat2 = conectorConCarla.getDatosVision()
    
    main = procesaImgCarla(main)
    lat1 = procesaImgCarlaPeq(lat1)
    lat2 = procesaImgCarlaPeq(lat2)

    # Sensores ODB
    velocidad = conectorConCarla.getVelocidad()
    acelerador = conectorConCarla.getAcelerador()
    freno = conectorConCarla.getFreno()
    anguloVolante = conectorConCarla.getVolante()
    


    # Tobii Driver Attention
    atencion_conductor = driverAttention.getDriverAttention()
    sin_atencion = driverAttention.getTimerAttention()


    #----------------Obtencion de datos---------------#

    #Object Detection
    objs1, outdetec1, fpsDet1 = detectorObjetos.deteccionRGBframe640(main)
    objs2, outdetec2, fpsDet2 = detectorObjetos.deteccionRGBframe320(lat1)
    objs3, outdetec3, fpsDet3 = detectorObjetos.deteccionRGBframe320(lat2)

    #Limite de velocidad obtenido del simulador
    limiteVelocidad = conectorConCarla.getLimiteVelocidad()



    #----------------Uso de los datos - Analisis ---------------#
    # Vista top-down 360º
    moduloTopDown.computaVistaTopDown(main, lat1, lat2)
    topDown = moduloTopDown.getVistaTopDown()

    # Lineas/carriles
    topDownMasked = moduloTopDown.getVistaTopDownEditada()


    # Analisis Semáforos
    semaforos = getSemaforos(objs1)
    analisisSemaf.stackAnalisisSemaforo(semaforos, main)
    semaforo = analisisSemaf.getStatusSemaforo()
    fps_semafs = analisisSemaf.getSemafFPS()

    #Interseccion
    analisisInterseccion.analisisDeInterseccion(moduloTopDown.getFrontMasked())
    interseccion = analisisInterseccion.getPrediccionInterseccion()
    fps_interseccion = analisisInterseccion.getFPS()

    #Marcas calzada
    inmediatamenteDelante = moduloTopDown.getInmediatamentedelante()
    ModulomarcasCalzada.analisisMarcasCalzada(inmediatamenteDelante)
    calzada = ModulomarcasCalzada.getMarcasCalzada()

    pasoPeatones = calzada['cebra']
    senyalStop = calzada['stop']
    senyalizquierda = calzada['senyalizquierda']
    senyalderecha = calzada['senyalderecha']
    senyaldelanteDer = calzada['delanteDerecha']
    senyaldelanteIzq = calzada['delanteIzq']

    #Road director
    roadDirector.analisisRD(inmediatamenteDelante)
    rd_wheel = roadDirector.getRDwheelNomalized()



    # Track y prediccion vehículos
    vehiculos = []
    for oj in objs1:
        if esVehiculo(oj.ClassID):
            v = Vehiculo(oj, random.randrange(10, 100))
            vehiculos.append(v)

    vehiculosTrackeados = []
    if vehiculosFrameAnterior == []:
        vehiculosFrameAnterior = vehiculos
    else:
        vehiculosTrackeados = algoritmoTrackingVehiculos(vehiculosFrameAnterior, vehiculos, limiteDistancia=200)
        vehiculosFrameAnterior = vehiculosTrackeados


    #Vehiculo cam lat 1
    vehiculoLat1 = []
    for oj in objs2:
        if esVehiculo(oj.ClassID):
            v = Vehiculo(oj, random.randrange(100, 199))
            vehiculoLat1.append(v)

    #Vehiculo cam lat 1
    vehiculoLat2 = []
    for oj in objs3:
        if esVehiculo(oj.ClassID):
            v = Vehiculo(oj, random.randrange(200, 299))
            vehiculoLat2.append(v)


    # Track y prediccion peatones
    peatones = []
    for oj in objs1:
        if esPeaton(oj.ClassID):
            v = Peaton(oj, random.randrange(10, 100))
            peatones.append(v)

    peatonesTrackeados = []
    if peatonesFrameAnterior == []:
        peatonesFrameAnterior = peatones
    else:
        peatonesTrackeados = algoritmoTrackingVehiculos(
            peatonesFrameAnterior, peatones, limiteDistancia=300)
        peatonesFrameAnterior = peatonesTrackeados



# Toma de decisiones
    #Por encima del limite de velocidad
    if limiteVelocidad is not None:
        if velocidad > limiteVelocidad:
            porEncimalimiteVel = True
            sonidos.reproduceAlertaQuindarEnd()
        else:
            porEncimalimiteVel = False
    else:
        porEncimalimiteVel = False

    #Peatones cerca del centro de la calzada
    for p in peatonesTrackeados:
        if abs(p.getCentroHorizPredict() - 320) < 300:
            if p.getArea_nv() > 4000:
                print('Peaton delante')
                pasoPeatones = True



    #Notificador
    notificaConductorSinAtencion = False
    if sin_atencion > 1.5:
        notificaConductorSinAtencion = True
        sonidos.reproduceAlertaQuindarStart()
        sonidos.reproduceAlertaQuindarEnd()

    # Cambio de Semaforo

    if estadoAnteriorSemaf is None:
        estadoAnteriorSemaf = semaforo
    else:
        if estadoAnteriorSemaf is not semaforo:
            if semaforo: #Verde
                print('El semaforo ha cambiado a verde')
                sonidos.reproduceAlertaQuindarStart()
                notificacionSemaforoEnVerde = True
            else:
                print('Se ha dejado de ver el semaforo')
                notificacionSemaforoEnVerde = False
        else:
            notificacionSemaforoEnVerde = notificacionSemaforoEnVerde


        estadoAnteriorSemaf = semaforo
            

    #Vehiculos punto muerto lat 1
    vehiculoCercaLat1, vehiculoCercaLat2 = False, False

    for v in vehiculoLat1:
        if v.getArea_nv() > 5000:
            vehiculoCercaLat1 = True
            
    for v in vehiculoLat2:
        if v.getArea_nv() > 5000:
            vehiculoCercaLat2 = True



# Notificaciones y GUI
    # Sonido

    # Pantalla

    # OpenCV
    datosOverlay = [semaforos, analisisSemaf.getPadding(
    ), vehiculosTrackeados, peatonesTrackeados, vehiculoLat1, vehiculoLat2]
    main = overlays.overlayInfoMain(main, datosOverlay)
    lat1 = overlays.overlayInfoSide1(lat1, datosOverlay)
    lat2 = overlays.overlayInfoSide2(lat2, datosOverlay)

    # Qt

    fps_vision = 1 / (time.time() - start_time)
    datosParaQT = [main, lat1, lat2, velocidad, atencion_conductor, fps_vision, topDown,
                   topDownMasked, semaforo,  0.0, fps_semafs, 0, interseccion, fps_interseccion, pasoPeatones, senyalStop, acelerador, freno, anguloVolante, rd_wheel, notificaConductorSinAtencion, notificacionSemaforoEnVerde, limiteVelocidad, porEncimalimiteVel, senyalizquierda, senyalderecha, senyaldelanteDer, senyaldelanteIzq, vehiculoCercaLat1, vehiculoCercaLat2]
    gui.actualizaInfoGui(datosParaQT)


    #Recordatorio para bucle OpenCV
    cv2.imshow('Recordatorio Aplicación', gui.getImgBucleCV())
    
    #Break del loop de OpenCV
    if chr(cv2.waitKey(1) & 255) == 'q':
        break
#---------------------------------------------

# Cerramos GUI
#gui.cierraGui()

# Desconectamos los sensores
conectorConCarla.desconectarDatosVision()
driverAttention.desconecta()

# Jetson Inference se desconecta automaticamente.
# Cerramos ventanas de OpenCV
cv2.destroyAllWindows()

print('Reproduciendo sonido de warning')
playsound('resources/quindarTones/end.ogg')

print('Adios!')
