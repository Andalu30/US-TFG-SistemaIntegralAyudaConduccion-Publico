
from RecolectorDatos import connectCARLAcompleto
from FuncionesAuxiliares import *
from UsoDatos import VistaTopDown

import cv2
import csv
import time
import random


conectorConCarla = connectCARLAcompleto('10.0.0.6', 'tesla.model3')

path = 'resources/datasetRoadDirector/5/'


archivo = open(f'{path}dataset.csv', 'w', newline='')
writer = csv.writer(archivo)
moduloTopDown = VistaTopDown()


i = 0
while True:

    main, lat1, lat2 = conectorConCarla.getDatosVision()
    main = procesaImgCarla(main)
    lat1 = procesaImgCarlaPeq(lat1)
    lat2 = procesaImgCarlaPeq(lat2)

    moduloTopDown.computaVistaTopDown(main, lat1, lat2)
    inmediatamenteDelante = moduloTopDown.getInmediatamentedelante()

    cv2.imshow('inmediatamenteDelante', inmediatamenteDelante)

    acelerador = conectorConCarla.getAcelerador()
    anguloVolante = conectorConCarla.getVolante()
    
    velocidad = conectorConCarla.getVelocidad()



    if velocidad > 3:

        print(f'Acel: {acelerador}, Volante: {anguloVolante}')
        filename_img = f'img_datRD_{i}'
        i = i+1

        cv2.imwrite(f'{path}{filename_img}.png', inmediatamenteDelante)
        writer.writerow([f"{filename_img}", f"{anguloVolante}", f"{acelerador}"])


        time.sleep(random.randint(1,3))
    else:
        print("Vehiculo detenido")

    #Break del loop de OpenCV
    if chr(cv2.waitKey(1) & 255) == 'q':
        break

conectorConCarla.desconectarDatosVision()
