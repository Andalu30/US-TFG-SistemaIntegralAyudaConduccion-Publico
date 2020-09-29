import cv2
import numpy as np
import pandas as pd

# DaySequence 1

path_ini_img = '/mnt/Datos/Descargas/LISA traffic light dataset/daySequence1/daySequence1/frames'
annotations_path = '/mnt/Datos/Descargas/LISA traffic light dataset/Annotations/Annotations/daySequence1/frameAnnotationsBOX.csv'

path_save = '/mnt/Datos/Descargas/LISA traffic light dataset/test/img/'


annotations = pd.read_csv(annotations_path, sep=';')

cantidad = len(annotations)
path_imgs = annotations['Filename']
path_imgs = list(map(lambda x : x[7:], path_imgs))

uly = annotations['Upper left corner Y']
lry = annotations['Lower right corner Y']

ulx = annotations['Upper left corner X']
lrx = annotations['Lower right corner X']


redgreens = annotations['Annotation tag']



imgData = []
imgLabel = []


for i in range(len(annotations)):
    path_img = path_ini_img+path_imgs[i]

    img = cv2.imread(path_img)

    coordRecorte = (uly[i],lry[i],ulx[i],lrx[i])
    recorte = img[coordRecorte[0]:coordRecorte[1], coordRecorte[2]:coordRecorte[3]]

    imgData.append(recorte)
    imgLabel.append(redgreens[i])



print(np.shape(imgData))
print(np.shape(imgLabel))

