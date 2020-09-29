import numpy as np
import numpy.polynomial.polynomial as poly
import random

from collections import deque


#Funciones auxiliares
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


class Semaforo:

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

        #Verde o Rojo?
        self.luz = None

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

    def getPrediccion(self):
        return (self.predictTop, self.predictBottom, self.predictLeft, self.predictRight)

    def getPrediccionKalman(self):
        pass
        # (top, bottom, left, right)


    def getColor(self):
        return self.luz

    def setColor(self, color):
        self.luz = color


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
