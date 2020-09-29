import threading
import queue
import cv2
import numpy as np

from openni import openni2
from openni import _openni2 as c_openni


class inputDatosVision:

    def __init__(self, dispCap1, dispCap2, openniStream='RGB'):
        
        self.openniStream = openniStream
        
        # Queue
        self.q = queue.Queue()

        # OpenCV
        self.cap1 = cv2.VideoCapture(dispCap1)
        self.cap2 = cv2.VideoCapture(dispCap2)

        # Openni
        openni2.initialize()
        dev = openni2.Device.open_any()
        
        self.depth_stream = dev.create_depth_stream()
        self.depth_stream.set_video_mode(c_openni.OniVideoMode(pixelFormat = c_openni.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM, resolutionX = 640, resolutionY = 480, fps = 30))
        self.depth_stream.start()

        # Openni IR/RGB
        if openniStream == 'IR':
            self.ir_stream = dev.create_ir_stream()
            self.ir_stream.set_video_mode(c_openni.OniVideoMode(pixelFormat=c_openni.OniPixelFormat.ONI_PIXEL_FORMAT_GRAY16, resolutionX=640, resolutionY=480, fps=30))
            self.ir_stream.start()

        else: # openniStream == 'RGB':
            self.color_stream = dev.create_color_stream()
            self.color_stream.set_video_mode(c_openni.OniVideoMode(pixelFormat = c_openni.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 640, resolutionY = 480, fps = 30))
            self.color_stream.start()






        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()


    def _funcion(self):
        while True:
            # OpenCV
            ret1, frame1 = self.cap1.read()
            ret2, frame2 = self.cap2.read()

            # Openni - Depth
            frame = self.depth_stream.read_frame()
            frame_data = frame.get_buffer_as_uint16() # Esto es un buffer, hay que convertirlo

            img = np.frombuffer(frame_data, dtype=np.uint16)
            img.shape = (480, 640) # Matriz con los datos de depth. El valor es la distancia en milímetros
            # Normalizamos los valores para poder representarlos
            depth = 1 - (img.astype(np.float) / np.max(img)) # Blanco = cerca + sombra, negro = lejos
            

            if self.openniStream == 'IR':
                frame = self.ir_stream.read_frame()
                frame_data = frame.get_buffer_as_uint16()

                img = np.frombuffer(frame_data, dtype=np.uint16)
                img.shape = (480,640)
                
                img = img.astype(np.float) / np.max(img)
                openniSelecStream = img
            
            elif self.openniStream == 'RGB':
                frame = self.color_stream.read_frame()
                frame_data = frame.get_buffer_as_uint8()

                img = np.frombuffer(frame_data, dtype=np.uint8)
                img.shape = (480,640,3) # RGB -> 3dimensional

                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # Convertimos a BGR porque es el standard de OpenCV
                openniSelecStream = img




            # Queue
            if not ret1 or not ret2:
                print("Error al adquirir señales de las camaras")
                self.desconectarDatosVision()

            if not self.q.empty():
                try:
                    self.q.get_nowait() # descartamos ultimos frames
                except queue.Empty:
                    pass
            self.q.put([frame1, frame2, depth, openniSelecStream])

    def read(self):
        return self.q.get()

    def getTipoStream(self):
        return self.openniStream

    def desconectarDatosVision(self):
        # OpenCV
        self.cap1.release()
        self.cap2.release()
        
        # Openni
        self.depth_stream.stop()

        if self.openniStream == 'IR':
            self.ir_stream.stop()
        else:
            self.color_stream.stop()
        openni2.unload()




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
