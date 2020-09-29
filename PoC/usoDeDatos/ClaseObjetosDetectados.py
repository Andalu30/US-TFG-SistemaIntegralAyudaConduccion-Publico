import numpy as np
import random

from collections import deque



#Funciones auxiliares
def centroPersonal(objNvidia):
    (x, y) = objNvidia.Center
    # Pasamos el centro a int
    x, y = int(x), int(y)
    return (x,y)

class Vehiculo:

    def __init__(self, objNvidia, idLoop):
        # Datos NVIDIA
        self.Area = objNvidia.Area
        self.Bottom = objNvidia.Bottom
        self.Center = objNvidia.Center
        self.ClassID = objNvidia.ClassID
        self.Confidence = objNvidia.Confidence
        self.Height = objNvidia.Height
        self.Instance = objNvidia.Instance
        self.Left = objNvidia.Left
        self.Right = objNvidia.Right
        self.Top = objNvidia.Top
        self.Width = objNvidia.Width

        # Datos personales
        self.Centro = centroPersonal(objNvidia)
        self.ID = idLoop
        self.numeroFramesSinDeteccionNueva = 0 # Para controlar frames en los que no se detecte

        # Memorias de las ultimas 50 posiciones (aprox 0.3s en modo MAX0)
        self.memoriaTop = deque([], 50)
        self.memoriaTop.append(objNvidia.Top)

        self.memoriaBottom = deque([], 50)
        self.memoriaBottom.append(objNvidia.Bottom)
        
        self.memoriaRight = deque([], 50)
        self.memoriaRight.append(objNvidia.Right)

        self.memoriaLeft = deque([], 50)
        self.memoriaLeft.append(objNvidia.Left)

    
    def relacionaConDeteccionNueva(self, objNuevo):
        # Actualizacion de info deteccion
        self.Area = objNuevo.Area
        self.Bottom = objNuevo.Bottom
        self.Center = objNuevo.Center
        self.ClassID = objNuevo.ClassID
        self.Confidence = objNuevo.Confidence
        self.Height = objNuevo.Height
        self.Instance = objNuevo.Instance
        self.Left = objNuevo.Left
        self.Right = objNuevo.Right
        self.Top = objNuevo.Top
        self.Width = objNuevo.Width

        self.Centro = centroPersonal(objNuevo)

        # Añadir a memoria
        self.memoriaTop.append(objNuevo.Top)
        self.memoriaBottom.append(objNuevo.Bottom)
        self.memoriaRight.append(objNuevo.Right)
        self.memoriaLeft.append(objNuevo.Left)

        print(f'MemoriaBott-{self.memoriaBottom}')

        # Actualizacion prediccion Kalman filter
        # if self.memoriaBottom.


    
    def noRelacionaConNuevo(self):
        self.numeroFramesSinDeteccionNueva += 1

        # Actualizacion de info deteccion con la prediccion!
        self.Confidence = 0.00
        # self.Top = 
        # self.Bottom =
        # self.Left = 
        # self.Right = 

        return self.numeroFramesSinDeteccionNueva
        





    def getID(self):
        return self.ID
    def setID(self, id):
        self.ID = id

    def getCentro(self):
        return self.Centro

    def getPrediccionKalman(self):
        pass
        # (top, bottom, left, right)




    # Nvidia getters
    def getArea_nv(self):
        return self.Area
    
    def getBottom_nv(self):
        return self.Bottom
    
    def getCenter_nv(self):
        return self.Center

    def getClassID_nv(self):
        return self.ClassID

    def getConfidence_nv(self):
        return self.Confidence

    def getHeight_nv(self):
        return self.Height
    
    def getInstance_nv(self):
        return self.Instance

    def getLeft_nv(self):
        return self.Left
    
    def getRight_nv(self):
        return self.Right

    def getTop_nv(self):
        return self.Top

    def getWidth_nv(self):
        return self.Width














class Peaton:
    pass








# Algoritmos de Tracking
def algoritmoTrackingVehiculos(vehiculosFrameAnterior, vehiculosFrameActual, limiteDistancia):



    def calculaMasCercanoAnterior(lista, indiv):

        indiv_centro = indiv.getCentro()
        lista_centros = list(map(lambda x: x.getCentro(), lista))

        distancias = []
        for centro in lista_centros:
            dist = np.sqrt( (indiv_centro[0] - centro[0])**2 + (indiv_centro[1] - centro[1])**2 ) # Distancia euclidea entre los centros
            distancias.append(dist)

        print(f' distancias -> {distancias}')


        dist_minima = np.min(distancias)
        arg_min = np.argmin(distancias)
        res = lista[arg_min]

        print(f'mascercanoAnterior = {res}, distancia = {dist_minima}')
        return res, dist_minima





    res = []

    # Para los nuevos, comprobamos si son alguno de los anteriores y los relacionamos
    vactualaasignados = []

    for nuevo in vehiculosFrameActual:
        if vehiculosFrameAnterior == []:
            break

        masCercanoAnterior, distancia = calculaMasCercanoAnterior(vehiculosFrameAnterior, nuevo)

        if distancia <= limiteDistancia:
            masCercanoAnterior.relacionaConDeteccionNueva(nuevo)

            vehiculosFrameAnterior.remove(masCercanoAnterior) # Eliminamos al anterior puesto que ya se ha relacionado
            vactualaasignados.append(nuevo)
            res.append(masCercanoAnterior)

    # Para los que no se relacionan, dependiendo del numero de frames que lleven sin relacion se olvidan o no
    for v in vehiculosFrameAnterior:
        
        if v not in res:
            a = v.noRelacionaConNuevo()
            if a <= 10: # 10 frames de margen
                res.append(v)

    # Para los que aparecen por primera vez en el frame nuevo (no se relacionan con ninguno anterior)
    for v in vehiculosFrameActual:
        if v not in vactualaasignados:
            v.setID(random.randrange(10,100))
            res.append(v)
        

    return res