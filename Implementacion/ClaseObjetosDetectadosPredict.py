import numpy as np
import numpy.polynomial.polynomial as poly
import random
import matplotlib.pyplot as plt

from collections import deque

#Funcion Auxiliar
def centroPersonal(objNvidia):
    (x, y) = objNvidia.Center
    # Pasamos el centro a int
    x, y = int(x), int(y)
    return (x, y)



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


        # Memorias de las ultimas 8 posiciones
        self.memoriaTop = deque([], 8)
        self.memoriaTop.append(objNvidia.Top)

        self.memoriaBottom = deque([], 8)
        self.memoriaBottom.append(objNvidia.Bottom)
        
        self.memoriaRight = deque([], 8)
        self.memoriaRight.append(objNvidia.Right)

        self.memoriaLeft = deque([], 8)
        self.memoriaLeft.append(objNvidia.Left)

        # Prediccion -> Inicialmente el mismo 
        self.predictTop = int(objNvidia.Top)
        self.predictBottom = int(objNvidia.Bottom)
        self.predictLeft = int(objNvidia.Left)
        self.predictRight = int(objNvidia.Right)

        self.AcercandoseOalejandose = None


    
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

        # Actualizacion prediccion
        if len(self.memoriaTop) >= 8:
            
            x = [x for x in range(8)]
            v = 15

            #Top
            y = self.memoriaTop
            coefs = poly.polyfit(x,y,1)
            ffit = poly.Polynomial(coefs)
            predict = int(ffit(v))
            self.predictTop = predict

            #Bottom
            y = self.memoriaBottom
            coefs = poly.polyfit(x,y,1)
            ffit = poly.Polynomial(coefs)
            predict = int(ffit(v))
            self.predictBottom =  predict

            #Left
            y = self.memoriaLeft
            coefs = poly.polyfit(x,y,1)
            ffit = poly.Polynomial(coefs)
            predict = int(ffit(v))
            self.predictLeft = predict
            
            #Right
            y = self.memoriaRight
            coefs = poly.polyfit(x,y,1)
            ffit = poly.Polynomial(coefs)
            predict = int(ffit(v))
            self.predictRight =  predict

            #Acercandose o Alejandose
            ancho_actual = self.Right - self.Left
            ancho_predict = self.predictRight - self.predictLeft

            aOa = ancho_actual - ancho_predict

            if abs(aOa) < 12: #Si no hay una diferencia de al menos 12 consideramos quieto
                self.AcercandoseOalejandose = None
            else:
                if aOa < 0:
                    self.AcercandoseOalejandose = '+'
                else:
                    self.AcercandoseOalejandose = '-'

        
        else: # Si todavia no lo he visto 5 frames
            # Prediccion -> Inicialmente el mismo 
            self.predictTop = int(self.Top)
            self.predictBottom = int(self.Bottom)
            self.predictLeft = int(self.Left)
            self.predictRight = int(self.Right)


    
    def noRelacionaConNuevo(self):
        self.numeroFramesSinDeteccionNueva += 1
        self.AcercandoseOalejandose = None

        # Actualizacion de info deteccion con la prediccion!
        self.Confidence = 0.00
        self.Top = self.predictTop
        self.Bottom = self.predictBottom
        self.Left = self.predictLeft
        self.Right = self.predictRight

        return self.numeroFramesSinDeteccionNueva
        
        
    def getAcercandoseOalejandose(self):
        return self.AcercandoseOalejandose

    def getID(self):
        return self.ID

    def setID(self, id):
        self.ID = id

    def getCentro(self):
        return self.Centro

    def getPrediccion(self):
        return (self.predictTop, self.predictBottom, self.predictLeft, self.predictRight)



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
        # Para controlar frames en los que no se detecte
        self.numeroFramesSinDeteccionNueva = 0

        # Memorias de las ultimas 10 posiciones
        self.memoriaTop = deque([], 10)
        self.memoriaTop.append(objNvidia.Top)

        self.memoriaBottom = deque([], 10)
        self.memoriaBottom.append(objNvidia.Bottom)

        self.memoriaRight = deque([], 10)
        self.memoriaRight.append(objNvidia.Right)

        self.memoriaLeft = deque([], 10)
        self.memoriaLeft.append(objNvidia.Left)

        # Prediccion -> Inicialmente el mismo
        self.predictTop = int(objNvidia.Top)
        self.predictBottom = int(objNvidia.Bottom)
        self.predictLeft = int(objNvidia.Left)
        self.predictRight = int(objNvidia.Right)

        self.predictCentroHoriz = 0


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

        # Actualizacion prediccion
        if len(self.memoriaTop) >= 10:

            x = [x for x in range(10)]
            v = 15

            #Top
            y = self.memoriaTop
            coefs = poly.polyfit(x, y, 1)
            ffit = poly.Polynomial(coefs)
            predict = int(ffit(v))
            self.predictTop = predict

            #Bottom
            y = self.memoriaBottom
            coefs = poly.polyfit(x, y, 1)
            ffit = poly.Polynomial(coefs)
            predict = int(ffit(v))
            self.predictBottom = predict

            #Left
            y = self.memoriaLeft
            coefs = poly.polyfit(x, y, 1)
            ffit = poly.Polynomial(coefs)
            predict = int(ffit(v))
            self.predictLeft = predict

            #Right
            y = self.memoriaRight
            coefs = poly.polyfit(x, y, 1)
            ffit = poly.Polynomial(coefs)
            predict = int(ffit(v))
            self.predictRight = predict

            self.predictCentroHoriz = self.predictRight - self.predictLeft

        else:  # Si todavia no lo he visto 10 frames
            # Prediccion -> Inicialmente el mismo
            self.predictTop = int(self.Top)
            self.predictBottom = int(self.Bottom)
            self.predictLeft = int(self.Left)
            self.predictRight = int(self.Right)


    def noRelacionaConNuevo(self):
        self.numeroFramesSinDeteccionNueva += 1

        # Actualizacion de info deteccion con la prediccion!
        self.Confidence = 0.00
        self.Top = self.predictTop
        self.Bottom = self.predictBottom
        self.Left = self.predictLeft
        self.Right = self.predictRight

        return self.numeroFramesSinDeteccionNueva

    def getID(self):
        return self.ID

    def setID(self, id):
        self.ID = id

    def getCentro(self):
        return self.Centro

    def getCentroHorizPredict(self):
        return self.predictCentroHoriz

    def getPrediccion(self):
        return (self.predictTop, self.predictBottom, self.predictLeft, self.predictRight)

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








# Algoritmos de Tracking
def algoritmoTrackingVehiculos(vehiculosFrameAnterior, vehiculosFrameActual, limiteDistancia):



    def calculaMasCercanoAnterior(lista, indiv):

        indiv_centro = indiv.getCentro()
        lista_centros = list(map(lambda x: x.getCentro(), lista))

        distancias = []
        for centro in lista_centros:
            dist = np.sqrt( (indiv_centro[0] - centro[0])**2 + (indiv_centro[1] - centro[1])**2 ) # Distancia euclidea entre los centros
            distancias.append(dist)

        dist_minima = np.min(distancias)
        arg_min = np.argmin(distancias)
        res = lista[arg_min]

        return res, dist_minima

    def estaEnBorde(vehiculo):
        left = vehiculo.getLeft_nv()
        right = vehiculo.getRight_nv()

        if left <= 10 or right >= 630: #10 de margen
            return True
        else:
            return False





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
            if not estaEnBorde(v):
                if a <= 5:
                    res.append(v)
            elif estaEnBorde(v):
                if a <= 3:
                    res.append(v)

    # Para los que aparecen por primera vez en el frame nuevo (no se relacionan con ninguno anterior)
    for v in vehiculosFrameActual:
        if v not in vactualaasignados:
            v.setID(random.randrange(10,100))
            res.append(v)
        

    return res




def algoritmoTrackingPeatones(PeatonesFrameAnterior, peatonesFrameActual, limiteDistancia):


    def calculaMasCercanoAnterior(lista, indiv):

        indiv_centro = indiv.getCentro()
        lista_centros = list(map(lambda x: x.getCentro(), lista))

        distancias = []
        for centro in lista_centros:
            # Distancia euclidea entre los centros
            dist = np.sqrt((indiv_centro[0] - centro[0])
                           ** 2 + (indiv_centro[1] - centro[1])**2)
            distancias.append(dist)

        print(f' distancias -> {distancias}')

        dist_minima = np.min(distancias)
        arg_min = np.argmin(distancias)
        res = lista[arg_min]

        print(f'mascercanoAnterior = {res}, distancia = {dist_minima}')
        return res, dist_minima

    def estaEnBorde(peaton):
        left = peaton.getLeft_nv()
        right = peaton.getRight_nv()

        if left <= 10 or right >= 630:  # 10 de margen
            return True
        else:
            return False

    res = []

    # Para los nuevos, comprobamos si son alguno de los anteriores y los relacionamos
    vactualaasignados = []

    for nuevo in peatonesFrameActual:
        if peatonesFrameActual == []:
            break

        masCercanoAnterior, distancia = calculaMasCercanoAnterior(PeatonesFrameAnterior, nuevo)

        if distancia <= limiteDistancia:
            masCercanoAnterior.relacionaConDeteccionNueva(nuevo)

            # Eliminamos al anterior puesto que ya se ha relacionado
            PeatonesFrameAnterior.remove(masCercanoAnterior)
            vactualaasignados.append(nuevo)
            res.append(masCercanoAnterior)

    # Para los que no se relacionan, dependiendo del numero de frames que lleven sin relacion se olvidan o no
    for v in PeatonesFrameAnterior:

        if v not in res:
            a = v.noRelacionaConNuevo()
            if not estaEnBorde(v):
                if a <= 10:
                    res.append(v)
            elif estaEnBorde(v):
                if a <= 3:
                    res.append(v)

    # Para los que aparecen por primera vez en el frame nuevo (no se relacionan con ninguno anterior)
    for v in peatonesFrameActual:
        if v not in vactualaasignados:
            v.setID(random.randrange(10, 100))
            res.append(v)

    return res
