import glob
import os
import sys

try:
    sys.path.append(glob.glob('/home/andalu30/Escritorio/CARLA_0.9.9.4/PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random
import time

import threading
import queue
import numpy as np

import datetime

import cv2


def procesaImg(image):
    i = np.array(image.raw_data)  # convert to an array
    # was flattened, so we're going to shape it.
    i2 = i.reshape((480, 640, 4))
    # remove the alpha (basically, remove the 4th index  of every pixel. Converting RGBA to RGB)
    i3 = i2[:, :, :3]
    return i3


class connectCARLA:
    
    def __init__(self, client):

        # Queue
        self.q = queue.Queue()

        self.actor_list = []

        client.set_timeout(2.0)
        world = client.get_world()




        actores = world.get_actors()
        print(actores)


        for actor in actores:
            print(dir(actor))
            print(actor.attributes)

            if 'model3' in actor.__str__():
                ego_coche = actor
                break
            else:
                ego_coche = None

        if ego_coche is not None:
            print('Se ha encontrado el vehiculo')
        else:
            print('No se ha encontrado el vehiculo')


        blueprint_library = world.get_blueprint_library()

        # Camara central
        camera_bp = blueprint_library.find('sensor.camera.rgb')

        camera_bp.set_attribute('image_size_x', '640')
        camera_bp.set_attribute('image_size_y', '480')
        camera_bp.set_attribute('fov', '56') #FOV 56 = PS Eye sin zoom
                                             #FOV 55 = Aukey


        camera_transform_central = carla.Transform(carla.Location(x=0.40, y=0.0, z=1.25))  # Respecto al parent
        camera = world.spawn_actor(camera_bp, camera_transform_central, attach_to=ego_coche)

        self.actor_list.append(camera)



        

        
        self.sensors = [camera]

        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()


    def _funcion(self):
        self.sensors[0].listen(lambda image: self.q.put(image))     # main

        # Queue
        if not self.q.empty():
            try:
                self.q.get_nowait() # descartamos ultimos frames
            except queue.Empty:
                pass

    def getDatosVision(self):
        return self.q.get()

    def desconectarDatosVision(self):
        print('Destruyendo actores', end='')
        for actor in self.actor_list:
            actor.destroy()
            print(".",end='')
        print('OK')
        



# Ejemplo de uso--------------------
client = carla.Client('localhost', 2000)
carlaConn = connectCARLA(client)

while True:
    start_time = time.time()  # start time of the loop

    central  = carlaConn.getDatosVision()
    central = procesaImg(central)

    cv2.imshow('Central', central)


    if chr(cv2.waitKey(1)&255) == 'q':
        break

cv2.destroyAllWindows()
carlaConn.desconectarDatosVision()
