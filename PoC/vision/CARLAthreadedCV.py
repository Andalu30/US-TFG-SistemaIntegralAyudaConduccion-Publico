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
    i2 = i.reshape((600, 800, 4))
    # remove the alpha (basically, remove the 4th index  of every pixel. Converting RGBA to RGB)
    i3 = i2[:, :, :3]
    return i3


class inputDatosVision:
    
    def __init__(self):

        # Queue
        self.q = queue.Queue()
        self.actor_list = []

        client = carla.Client('localhost', 2000)
        # client.set_timeout(40.0)
        world = client.get_world()


        #Opciones de mundo

        #Fixed time step
        settings = world.get_settings()
        settings.fixed_delta_seconds = 1
        world.apply_settings(settings)

        #Syncronous with client
        settings = world.get_settings()
        settings.synchronous_mode = True  # Enables synchronous mode
        world.apply_settings(settings)
        world.on_tick(lambda x: print('.',end=''))




        blueprint_library = world.get_blueprint_library()

        bp = random.choice(blueprint_library.filter('vehicle'))
        bp_tesla = random.choice(blueprint_library.filter('model3'))

        spawn = random.choice(world.get_map().get_spawn_points())

        tesla = world.spawn_actor(bp_tesla, spawn)
        self.actor_list.append(tesla)
        print(f'Se ha creado {tesla.type_id}')

        tesla.set_autopilot(True)

        camera_bp = blueprint_library.find('sensor.camera.rgb')
        camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))  # Respecto al coche
        camera = world.spawn_actor(camera_bp, camera_transform, attach_to=tesla)
        self.actor_list.append(camera)
        print(f'Se ha creado {camera.type_id}')

        self.camera = camera

        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()


    def _funcion(self):
        self.camera.listen(lambda image: self.q.put(procesaImg(image)))


        # Queue
        if not self.q.empty():
            try:
                self.q.get_nowait() # descartamos ultimos frames
            except queue.Empty:
                pass


    def read(self):
        return self.q.get()


    def desconectarDatosVision(self):
        print('Destruyendo actores', end='')
        for actor in self.actor_list:
            actor.destroy()
            print(".",end='')
        print('OK')
        



# Ejemplo de uso--------------------
client = carla.Client('localhost', 2000)
world = client.get_world()

visionData = inputDatosVision()

while True:
    world.tick()

    frame = visionData.read()
    cv2.imshow('frame1', frame)

    if chr(cv2.waitKey(16)&255) == 'q':
        break

cv2.destroyAllWindows()
visionData.desconectarDatosVision()
