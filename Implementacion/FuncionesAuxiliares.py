import numpy as np
import random
from ClasesAuxiliares import Semaforo
from ClaseObjetosDetectadosPredict import Vehiculo, Peaton



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


def estaEnBorde(vehiculo):
    left = vehiculo.getLeft_nv()
    right = vehiculo.getRight_nv()

    if left <= 10 or right >= 1910:  # 10 de margen
        return True
    else:
        return False


def esVehiculo(num):
    return (num in [2, 3, 4, 6, 8])


def esSemaforo(n):
    return n is 10


def esStop(n):
    return n is 13


def esPeaton(n):
    return n is 1


def centroPersonal(objNvidia):
    (x, y) = objNvidia.Center
    # Pasamos el centro a int
    x, y = int(x), int(y)
    return (x, y)


def procesaImgCarla(image):
    i = np.array(image.raw_data)  # convert to an array
    # was flattened, so we're going to shape it.
    i2 = i.reshape((480, 640, 4))
    # remove the alpha (basically, remove the 4th index  of every pixel. Converting RGBA to RGB)
    i3 = i2[:, :, :3]
    return i3


def procesaImgCarlaPeq(image):
    i = np.array(image.raw_data)  # convert to an array
    # was flattened, so we're going to shape it.
    i2 = i.reshape((240, 320, 4))
    # remove the alpha (basically, remove the 4th index  of every pixel. Converting RGBA to RGB)
    i3 = i2[:, :, :3]
    return i3



def getSemaforos(objsdetect):
    detectSenafs = list(filter(lambda x: esSemaforo(x.ClassID), objsdetect))
    res = []
    for semaf in detectSenafs:
        nuevo = Semaforo(semaf, random.randrange(10, 100))
        res.append(nuevo)
        
    return res


def getColorSemaforoFromPrediccion(prediccion, thresh=0.5):
    
    if prediccion[0]<thresh:
        return True
    else:
        return False


def getInterseccionFromPrediccion(prediccion, thresh=0.5):
    if prediccion[0][0] < thresh:
        return True
    else:
        return False


def getVehiculos(objs):
    vehiculos = []
    for oj in objs:
        if esVehiculo(oj.ClassID):
            v = Vehiculo(oj, random.randrange(10, 100))
            vehiculos.append(v)

    return vehiculos


def centroPersonal(objNvidia):
    (x, y) = objNvidia.Center
    # Pasamos el centro a int
    x, y = int(x), int(y)
    return (x, y)
