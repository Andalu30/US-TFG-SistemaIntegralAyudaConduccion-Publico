import jetson.inference
import jetson.utils

import multiprocessing
import numpy as np
import cv2
import tensorflow as tf
import time
import queue
from collections import deque
from PIL import Image, ImageOps


from FuncionesAuxiliares import *



class objectDetectionJetsonInference:

    def __init__(self, modelo='ssd-inception-v2', threshold=0.1):

        self.manager = multiprocessing.Manager()
        self.net = jetson.inference.detectNet(modelo, threshold)
        

    def deteccionRGBframe720(self, frame):
        # Lo convertimos a RGBA
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

        # Lo pasamos a CUDA para que se pueda usar con la net
        frame = jetson.utils.cudaFromNumpy(frame)

        detections = self.net.Detect(frame, 1280, 720) #Deteccion

        frame = jetson.utils.cudaToNumpy(frame, 1280, 720, 4)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)

        self.detections = detections
        self.frame = frame
        self.fps = self.net.GetNetworkFPS()

        return detections, frame, self.net.GetNetworkFPS()

    def deteccionRGBframe640(self, frame):
        # Lo convertimos a RGBA
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

        # Lo pasamos a CUDA para que se pueda usar con la net
        frame = jetson.utils.cudaFromNumpy(frame)

        detections = self.net.Detect(frame, 640, 480)

        frame = jetson.utils.cudaToNumpy(frame, 640, 480, 4)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)

        self.detections = detections
        self.frame = frame
        self.fps = self.net.GetNetworkFPS()

        return self.detections, self.frame, self.fps

    def deteccionRGBframe320(self, frame):
            # Lo convertimos a RGBA
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

        # Lo pasamos a CUDA para que se pueda usar con la net
        frame = jetson.utils.cudaFromNumpy(frame)

        detections = self.net.Detect(frame, 320, 240)

        frame = jetson.utils.cudaToNumpy(frame, 320, 240, 4)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)

        self.detections = detections
        self.frame = frame
        self.fps = self.net.GetNetworkFPS()

        return self.detections, self.frame, self.net.GetNetworkFPS()

    def getRes(self):
        return self.detections, self.frame, self.fps


class segmentationJetsonInference:

    def __init__(self, modelo='fcn-resnet18-cityscapes'):
        self.manager = multiprocessing.Manager()
        self.net = jetson.inference.segNet(modelo)

    def segmentRGBframe720(self, frame):

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
        frame = jetson.utils.cudaFromNumpy(frame)

        self.net.Process(frame, 1280, 720)
        self.net.Mask(frame, 1280, 720, 'point')

        frame = jetson.utils.cudaToNumpy(frame, 1280, 720, 4)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)

        frame = cv2.resize(frame,  (1280, 720))

        self.mascara = frame
        self.fps = self.net.GetNetworkFPS
        return frame, self.net.GetNetworkFPS()

    def segmentRGBframe640(self, frame):
        frame = cv2.resize(frame, (1024, 512))

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
        frame = jetson.utils.cudaFromNumpy(frame)


        self.net.Process(frame, 1024, 512)
        self.net.Mask(frame, 1024, 512, 'point')

        frame = jetson.utils.cudaToNumpy(frame, 1024, 512, 4)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)

        frame = cv2.resize(frame,  (640, 480))

        self.mascara = frame
        self.fps = self.net.GetNetworkFPS
        return frame, self.net.GetNetworkFPS()

    def getRes(self):
        return self.mascara, self.fps


class clasificacionSemaforos:

    def __init__(self, modelo='nuevoModeloBinario10epochs.h5', thresh=0.5, padding=3):
        self.semafModel = tf.keras.models.load_model(f'resources/ai_models/{modelo}')
        self.thresh= thresh

        self.paddingOriginal = padding
        self.padding = self.paddingOriginal

        self.fps = 0.0
        self.statusSemaforoQueue = deque([], 10)


    def stackAnalisisSemaforo(self, semaforos, main):
        start_time = time.time()

        self.padding = self.paddingOriginal

        if semaforos:

            semaforos.sort(key=lambda x: abs(x.getLeft_nv() - 320))
            semaforoPrincipal = semaforos[0]

            top = int(semaforoPrincipal.getTop_nv())
            bot = int(semaforoPrincipal.getBottom_nv())
            rig = int(semaforoPrincipal.getRight_nv())
            lef = int(semaforoPrincipal.getLeft_nv())
                
            if top < self.padding or bot > 480-self.padding or rig > 640-self.padding or lef < self.padding:
                self.padding = 0

            rgb_semafPrin = main[top-self.padding:bot+self.padding, lef-self.padding:rig+self.padding]

            rgb_semafPrin = cv2.resize(rgb_semafPrin, (25, 25))


            data = np.ndarray(shape=(1, 25, 25, 3), dtype=np.float32)
            data[0] = rgb_semafPrin

            infer = self.semafModel.signatures["serving_default"]
            labeling = infer(tf.constant(data, dtype=float))['activation_17']
            
            self.statusSemaforoQueue.append(
                getColorSemaforoFromPrediccion(labeling, self.thresh))

            self.fps = (1.0 / (time.time() - start_time))

        else:
            self.noHaySemaforo()


    def clasificaSemaforo(self, semaforoRGB):
        start_time = time.time()
        
        semaforoRGB = cv2.resize(semaforoRGB, (25, 25))
        data = np.ndarray(shape=(1, 25, 25, 3), dtype=np.float32)
        data[0] = semaforoRGB

        infer = self.semafModel.signatures["serving_default"]
        labeling = infer(tf.constant(data, dtype=float))['dense_21']
        self.statusSemaforoQueue.append(getColorSemaforoFromPrediccion(labeling, self.thresh))

        self.fps = (1.0 / (time.time() - start_time))
        

    def getStatusSemaforo(self):
        from collections import Counter
        c = Counter(list(self.statusSemaforoQueue))

        return c.most_common(1)[0][0]

    def getSemafFPS(self):
        return self.fps

    def noHaySemaforo(self):
        self.statusSemaforoQueue.append(None)

    def getPadding(self):
        return self.padding


class deteccionInterseccion:

    def __init__(self, modelo='modeloInterseccion',  thresh=0.5):
    
        self.interseccModel = tf.saved_model.load(f'resources/ai_models/{modelo}')
        self.thresh = thresh

        self.statusInterseccionQueue = deque([], 10)
        
        self.fps = 0.0


    def analisisDeInterseccion(self, img):

        start_time = time.time()

        img = cv2.resize(img, (100, 50))

        data = np.ndarray(shape=(1, 50, 100, 3), dtype=np.float32)
        data[0] = img

        infer = self.interseccModel.signatures["serving_default"]
        labeling = infer(tf.constant(data, dtype=float))['activation_42']
        self.statusInterseccionQueue.append(getInterseccionFromPrediccion(labeling, self.thresh))
        self.fps = (1.0 / (time.time() - start_time))


    def getPrediccionInterseccion(self):
        from collections import Counter
        c = Counter(list(self.statusInterseccionQueue))
        
        return c.most_common(1)[0][0]

    def getFPS(self):
        return self.fps



class RoadDirector:

    def __init__(self, modelo='RoadDirector-firstTry2slow'):
        
        self.RDmodel = tf.saved_model.load(f'resources/ai_models/{modelo}')
        self.roadDirectorWheel = None
        self.roadDirectorNormalizado = deque([], 10)
        self.fps = 0.0

    def analisisRD(self, img):
        start_time = time.time()

        img = cv2.resize(img, (200, 100))
        #normalized_image_array = (img.astype(np.float32) / 127.0) - 1

        data = np.ndarray(shape=(1, 100, 200, 3), dtype=np.float32)
        #data[0] = normalized_image_array
        data[0] = img

        infer = self.RDmodel.signatures["serving_default"]
        labeling = infer(tf.constant(data, dtype=float))['dense_39']
        self.roadDirectorWheel = labeling
        self.roadDirectorNormalizado.append(float(labeling[0]))

        self.fps = (1.0 / (time.time() - start_time))

    def getRDwheel(self):
        return self.roadDirectorWheel

    def getRDwheelNomalized(self):
        
        from statistics import mean
        return mean(self.roadDirectorNormalizado)
