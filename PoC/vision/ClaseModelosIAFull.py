import jetson.inference
import jetson.utils

import numpy as np
import cv2



class objectDetectionJetsonInference:

    def __init__(self, modelo='ssd-inception-v2', threshold=0.1):

        self.net = jetson.inference.detectNet(modelo, threshold)



    def deteccionRGBframe(self, image):
        frame = image
        #frame = cv2.resize(image, (640, 480))
        # Lo convertimos a RGBA
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

        # Lo pasamos a CUDA para que se puedea usar con la net
        frame = jetson.utils.cudaFromNumpy(frame)

        detections = self.net.Detect(frame, 1920, 1080)

        frame = jetson.utils.cudaToNumpy(frame, 1920, 1080, 4)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)

        cv2.putText(frame, f"FPS: {self.net.GetNetworkFPS()}", (25, 25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

        return detections, frame


    # def deteccionRGBAframe(self, image):

    #     frame = cv2.resize(image, (640, 480))

    #     # Lo pasamos a CUDA para que se puedea usar con la net
    #     frame = jetson.utils.cudaFromNumpy(frame)

    #     detections = self.net.Detect(frame, 640, 480)
    #     return detections


    # def deteccionCUDAframe(self, image):

    #     detections = self.net.Detect(frame, 640, 480)
    #     return detections










class segmentationJetsonInference:

    def __init__(self, modelo='fcn-resnet18-cityscapes'):

        self.net = jetson.inference.segNet(modelo)


    def segmentRGBframe(self, image):

        frame = image
        #frame = cv2.resize(image,  (640, 480))
        
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
        frame = jetson.utils.cudaFromNumpy(frame)

        self.net.Process(frame, 1920, 1080)
        self.net.Mask(frame, 1920, 1080, 'point')

        frame = jetson.utils.cudaToNumpy(frame, 1920, 1080, 4)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB).astype(np.uint8)

        frame = cv2.resize(frame,  (1920, 1080))

        cv2.putText(frame, f"FPS: {self.net.GetNetworkFPS()}",
                    (25, 25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

        return frame



    # def segmentRGBAframe(self, image):

    #     frame = cv2.resize(image, (640, 480))

    #     # Lo pasamos a CUDA para que se puedea usar con la net
    #     frame = jetson.utils.cudaFromNumpy(frame)

    #     detections = self.net.Detect(frame, 640, 480)
    #     return detections


    # def segmentCUDAframe(self, image):

    #     detections = self.net.Detect(frame, 640, 480)
    #     return detections
