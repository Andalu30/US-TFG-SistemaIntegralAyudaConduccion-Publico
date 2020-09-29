from openni import openni2
from openni import _openni2 as c_api

import sys
import numpy as np
import cv2



# Inicialización de Openni para trabajar con Asus Xtion y/o Kinect
openni2.initialize()

dev = openni2.Device.open_any()
print(dev.get_sensor_info(openni2.SENSOR_DEPTH))

# Activación de los streams de datos
# No se pueden activar al mismo tiempo RGB e IR !!

# Depth
depth_stream = dev.create_depth_stream()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM, resolutionX = 640, resolutionY = 480, fps = 30))
depth_stream.start()

# RGB
# color_stream = dev.create_color_stream()
# color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 640, resolutionY = 480, fps = 30))
# color_stream.start()


# IR
ir_stream = dev.create_ir_stream()
ir_stream.set_video_mode(c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_GRAY16, resolutionX=640, resolutionY=480, fps=30))
ir_stream.start()



while True:

    # Depth
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16() # Esto es un buffer, hay que convertirlo
    
    img = np.frombuffer(frame_data, dtype=np.uint16)
    img.shape = (480, 640) # Matriz con los datos de depth. El valor es la distancia en milímetros

    # Normalizamos los valores para poder representarlos
    img = 1 - (img.astype(np.float) / np.max(img)) # Blanco = cerca + sombra, negro = lejos


    cv2.imshow("Depth", img)




    # RGB    
    # frame = color_stream.read_frame()
    # frame_data = frame.get_buffer_as_uint8()

    # img = np.frombuffer(frame_data, dtype=np.uint8)
    # img.shape = (480,640,3) # RGB -> 3dimensional

    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # Convertimos a BGR porque es el standard de OpenCV

    # cv2.imshow("RGB", img)


#IR
    frame = ir_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()

    img = np.frombuffer(frame_data, dtype=np.uint16)
    # convert to 3-dimensional array
    img.shape = (480,640)
    
    img = img.astype(np.float) / np.max(img)
    cv2.imshow("IR", img)





    if cv2.waitKey(16) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

depth_stream.stop()
# color_stream.stop()
ir_stream.stop()


openni2.unload()
