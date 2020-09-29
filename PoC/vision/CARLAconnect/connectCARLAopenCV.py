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

import cv2


def procesaImg(image):
    i = np.array(image.raw_data)  # convert to an array
    # was flattened, so we're going to shape it.
    i2 = i.reshape((480, 640, 4))
    # remove the alpha (basically, remove the 4th index  of every pixel. Converting RGBA to RGB)
    i3 = i2[:, :, :3]
    return i3


def procesaImgPequeña(image):
    i = np.array(image.raw_data)  # convert to an array
    # was flattened, so we're going to shape it.
    i2 = i.reshape((240, 320, 4))
    # remove the alpha (basically, remove the 4th index  of every pixel. Converting RGBA to RGB)
    i3 = i2[:, :, :3]
    return i3


class connectCARLA:
    
    def __init__(self, client):

        # Queue
        self.q = queue.Queue()
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.q3 = queue.Queue()
        self.q4 = queue.Queue()


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



        # Camaras laterales
        camera_lateral_bp = blueprint_library.find('sensor.camera.rgb')

        camera_lateral_bp.set_attribute('image_size_x', '320')
        camera_lateral_bp.set_attribute('image_size_y', '240')
        camera_lateral_bp.set_attribute('fov', '56')    # FOV 56 = PS Eye sin zoom
                                                        # FOV 55 = Aukey

        camera_transform_lateral1 = carla.Transform(carla.Location(x=0.60, y=-0.85, z=1), carla.Rotation(roll=0, yaw=-150, pitch=0.0))  # Respecto al parent
        camera_transform_lateral2 = carla.Transform(carla.Location(x=0.60, y= 0.85, z=1), carla.Rotation(roll=0, yaw= 150, pitch=0.0))  # Respecto al parent

        camera_lateral1 = world.spawn_actor(camera_lateral_bp, camera_transform_lateral1, attach_to=ego_coche)
        camera_lateral2 = world.spawn_actor(camera_lateral_bp, camera_transform_lateral2, attach_to=ego_coche)


        self.actor_list.append(camera_lateral1)
        self.actor_list.append(camera_lateral2)


        # Semantic Segmentation Ground truth
        semantic_bp = blueprint_library.find('sensor.camera.semantic_segmentation')
        semantic_bp.set_attribute('image_size_x', '320')
        semantic_bp.set_attribute('image_size_y', '240')
        semantic_bp.set_attribute('fov', '56')

        semantic = world.spawn_actor(semantic_bp, camera_transform_central, attach_to=ego_coche)

        self.actor_list.append(semantic)


        # Depth estimation Ground Truth
        depth_bp = world.get_blueprint_library().find('sensor.camera.depth')
        depth_bp.set_attribute('image_size_x', '320')
        depth_bp.set_attribute('image_size_y', '240')
        depth_bp.set_attribute('fov', '56')

        depth_cam = world.spawn_actor(depth_bp, camera_transform_central, attach_to=ego_coche)

        self.actor_list.append(depth_cam)





        
        self.sensors = [camera, semantic, camera_lateral1, camera_lateral2, depth_cam]

        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()

        t2 = threading.Thread(target=self._funcion2)
        t2.daemon = True
        t2.start()


    def _funcion(self):
        self.sensors[0].listen(lambda image: self.q.put(image))     # main
        self.sensors[2].listen(lambda image: self.q2.put(image))    # lat1
        self.sensors[3].listen(lambda image: self.q3.put(image))    # lat2


        # Queue
        if not self.q.empty() or self.q2.empty or self.q3.empty:
            try:
                self.q.get_nowait() # descartamos ultimos frames
                self.q2.get_nowait()
                self.q3.get_nowait()
            except queue.Empty:
                pass

    def _funcion2(self):
        self.sensors[1].listen(lambda image: self.q1.put(image))    # semantic
        self.sensors[4].listen(lambda image: self.q4.put(image))    # depth


        # Queue
        if not self.q1.empty or self.q4.empty:
            try:
                self.q1.get_nowait()
                self.q4.get_nowait()
            except queue.Empty:
                pass

    def getDatosVision(self):
        return self.q.get(), self.q1.get(), self.q2.get(), self.q3.get(), self.q4.get()


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

    central, semantic, lat1, lat2, depth = carlaConn.getDatosVision()

    central = procesaImg(central)
    lat1 = procesaImgPequeña(lat1)
    lat2 = procesaImgPequeña(lat2)



    cv2.imshow('Central', central)
    cv2.imshow('Lateral1', lat1)
    cv2.imshow('Lateral2', lat2)

    semantic.convert(carla.ColorConverter.CityScapesPalette)
    depth.convert(carla.ColorConverter.LogarithmicDepth)

    semantic = procesaImgPequeña(semantic)
    cv2.imshow('Semantic Segmentation', semantic)

    depth = procesaImgPequeña(depth)
    cv2.imshow('Depth Estimation', depth)

    if chr(cv2.waitKey(1)&255) == 'q':
        break


cv2.destroyAllWindows()
carlaConn.desconectarDatosVision()
