import threading
import queue
import cv2
import numpy as np

class inputDatosVision:

    def __init__(self, dispCap1, dispCap2, dispCap3):
                
        # Queue
        self.q = queue.Queue()

        # OpenCV
            # Cap1 = Main = Aukey
        self.cap1 = cv2.VideoCapture(dispCap1)
        self.cap1.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
        self.cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

            # Cap2/3 = Sides = PS3eye
        self.cap2 = cv2.VideoCapture(dispCap2)
        self.cap2 = cv2.VideoCapture(dispCap3)

        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()


    def _funcion(self):
        while True:
            # OpenCV
            ret1, frame1 = self.cap1.read()
            ret2, frame2 = self.cap2.read()
            ret3, frame3 = self.cap3.read()


            # Queue
            if not ret1 or not ret2 or not ret3:
                print("Error al adquirir señales de las camaras")
                self.desconectarDatosVision()

            if not self.q.empty():
                try:
                    self.q.get_nowait() # descartamos ultimos frames
                except queue.Empty:
                    pass
            self.q.put((frame1, frame2, frame3))

    def read(self):
        return self.q.get()

    def desconectarDatosVision(self):
        # OpenCV
        self.cap1.release()
        self.cap2.release()
        self.cap3.release()



# Ejemplo de uso

# visionData = inputDatosVision(0,1,2)

# while True:
#     (frame1, frame2, frame3) = visionData.read()
#     time.sleep(0.01)
#     cv2.imshow('frame1', frame1)
#     cv2.imshow('frame2', frame2)
#     cv2.imshow('frame3', frame3)

#     if chr(cv2.waitKey(16)&255) == 'q':
#         break

# visionData.desconectarDatosVision()
