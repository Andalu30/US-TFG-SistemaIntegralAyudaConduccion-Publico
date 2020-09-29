import threading
import queue
import cv2
import numpy as np


class inputDatosVision:

    def __init__(self, carpeta):
        
        # Queue
        self.q = queue.Queue()

        # OpenCV
        self.cap1 = cv2.VideoCapture(f"{carpeta}/main.avi")
        self.cap2 = cv2.VideoCapture(f"{carpeta}/side1.avi")
        self.cap3 = cv2.VideoCapture(f"{carpeta}/side2.avi")

        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()


    def _funcion(self):
        while True:
            # OpenCV
            ret1, main = self.cap1.read()
            ret2, side1 = self.cap2.read()
            ret3, side2 = self.cap3.read()


            # Queue
            if not ret1 or not ret2 or not ret3:
                print("Error al adquirir señales de las camaras")
                self.desconectarDatosVision()

            if not self.q.empty():
                try:
                    self.q.get_nowait() # descartamos ultimos frames
                except queue.Empty:
                    pass
            self.q.put((main, side1, side2))

    def read(self):
        return self.q.get()

    def desconectarDatosVision(self):
        # OpenCV
        self.cap1.release()
        self.cap2.release()
        self.cap3.release()




# Ejemplo de uso

# visionData = inputDatosVision(0,2,openniStream='IR')

# while True:
#     [frame1, frame2, depth, opennistream] = visionData.read()
#     time.sleep(0.01)
#     cv2.imshow('frame1', frame1)
#     cv2.imshow('frame2', frame2)
#     cv2.imshow('depth', depth)
#     cv2.imshow('stream', opennistream)


#     if chr(cv2.waitKey(16)&255) == 'q':
#         break

# visionData.desconectarDatosVision()
