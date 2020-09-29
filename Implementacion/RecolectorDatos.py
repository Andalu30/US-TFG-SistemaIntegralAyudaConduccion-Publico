import threading
import queue
import cv2
import sys
import glob
import math
import time

import socket
import carla

# try:
#     sys.path.append(glob.glob('CARLA_dists/carla-*%d.%d-%s.egg' % (
#         sys.version_info.major,
#         sys.version_info.minor,
#         'linux-x86_64'))[0])
 
# except IndexError:
#     pass



class inputDatosVision:
    """Clase encargada de recoger los datos de las cámaras y ponerlos a disposicion de quien la llame"""

    def __init__(self, dispCap1, dispCap2, dispCap3):

        # Queue
        self.q = queue.Queue()

        # OpenCV
        # Cap1 = Main = Aukey
        self.cap1 = cv2.VideoCapture(dispCap1)
        self.cap1.set(cv2.CAP_PROP_FOURCC,
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

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
                raise Exception("Error al adquirir señales de las camaras")
                self.desconectarDatosVision()

            if not self.q.empty():
                try:
                    self.q.get_nowait()  # descartamos ultimos frames
                except queue.Empty:
                    pass
            self.q.put(frame1, frame2, frame3)

    def read(self):
        return self.q.get()

    def desconectarDatosVision(self):
        # OpenCV
        self.cap1.release()
        self.cap2.release()
        self.cap3.release()


class inputDatosVisionMainSolo:
    """Igual que inputDatosVision pero unicamente para la cámara principal. Las otras camaras son None."""

    def __init__(self, dispCap1):

        # Queue
        self.q = queue.Queue()

        # OpenCV
        # Cap1 = Main = Aukey
        self.cap1 = cv2.VideoCapture(dispCap1)
        self.cap1.set(cv2.CAP_PROP_FOURCC,
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()

    def _funcion(self):
        while True:
            # OpenCV
            ret1, frame1 = self.cap1.read()

            # Queue
            if not ret1 or not ret2 or not ret3:
                raise Exception("Error al adquirir señales de las camaras")
                self.desconectarDatosVision()

            if not self.q.empty():
                try:
                    self.q.get_nowait()  # descartamos ultimos frames
                except queue.Empty:
                    pass
            self.q.put(frame1, None, None)

    def read(self):
        return self.q.get()

    def desconectarDatosVision(self):
        # OpenCV
        self.cap1.release()


class inputDatosVisionSimul:
    """Igual que la clase inputDatosVision pero para simulaciones. El constructor recibe la carpeta con los archivos de video"""

    def __init__(self, carpeta, resolucion):

        # Queue
        self.q = queue.Queue()

        # OpenCV
        self.cap1 = cv2.VideoCapture(f"{carpeta}/main.avi")
        self.cap2 = cv2.VideoCapture(f"{carpeta}/side1.avi")
        self.cap3 = cv2.VideoCapture(f"{carpeta}/side2.avi")

        self.resolucion = resolucion

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

            main = cv2.resize(main, self.resolucion)
            # side1 = cv2.resize(side1, self.resolucion)
            # side2 = cv2.resize(side2, self.resolucion)


            if not self.q.empty():
                try:
                    self.q.get_nowait()  # descartamos ultimos frames
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


class inputDatosVisionMainSimul:
    """Igual que inputDatosVisionSimul pero unicamente para la cámara principal. Las otras camaras son None."""

    def __init__(self, carpeta, resolucion):

        # Queue
        self.q = queue.Queue()

        # OpenCV
        # Cap1 = Main = Aukey
        self.cap1 = cv2.VideoCapture(f"{carpeta}/main.avi")

        self.resolucion = resolucion

        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()

    def _funcion(self):
        while True:
            # OpenCV
            ret1, frame1 = self.cap1.read()

            # Queue
            if not ret1:
                raise Exception("Error al adquirir señales de las camaras")
                self.desconectarDatosVision()


            frame1 = cv2.resize(frame1, self.resolucion) #Casi 100 frames mas lento!!


            if not self.q.empty():
                try:
                    self.q.get_nowait()  # descartamos ultimos frames
                except queue.Empty:
                    pass
            self.q.put((frame1, None, None))

    def read(self):
        return self.q.get()

    def desconectarDatosVision(self):
        # OpenCV
        self.cap1.release()


class connectCARLAsimple:

    def __init__(self, ip, coche='tesla.model3'):

        # Queue
        self.q = queue.Queue()

        self.actor_list = []


        client = carla.Client(ip, 2000)
        client.set_timeout(2.0)
        world = client.get_world()



        actores = world.get_actors()

        for actor in actores:
            if coche in actor.__str__():
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
        camera_bp.set_attribute('fov', '56')  # FOV 56 = PS Eye sin zoom
        #FOV 55 = Aukey

        camera_transform_central = carla.Transform(
            carla.Location(x=0.40, y=0.0, z=1.35))  # Respecto al parent
        camera = world.spawn_actor(
            camera_bp, camera_transform_central, attach_to=ego_coche)

        self.actor_list.append(camera)

        self.sensors = [camera]

        # Thread
        t = threading.Thread(target=self._funcion)
        t.daemon = True
        t.start()

    def _funcion(self):

        def siempreUltimoFrame(imagen,q):
            if not q.empty():
                try:
                    q.get_nowait()  # descartamos ultimos frames
                except queue.Empty:
                    pass
            q.put(imagen)

        self.sensors[0].listen(lambda image: siempreUltimoFrame(image, self.q))
        
    def getDatosVision(self):
        return self.q.get()

    def read(self):
        return self.q.get()

    def desconectarDatosVision(self):
        print('Destruyendo actores', end='')
        for actor in self.actor_list:
            actor.destroy()
            print(".", end='')
        print('OK')


class connectCARLAcompleto:

    def __init__(self, ip, coche='tesla.model3'):

        # Queue
        self.q = queue.Queue()
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

        self.velocidad = None
        self.acelerador = None
        self.freno = None
        self.volante = None
        self.limiteVelocidad = None


        self.actor_list = []

        client = carla.Client(ip, 2000)
        client.set_timeout(2.0)
        world = client.get_world()
        self.world = world

        actores = world.get_actors()
        print(actores)

        for actor in actores:
            print(dir(actor))
            print(actor.attributes)

            if coche in actor.__str__():
                ego_coche = actor
                break
            else:
                ego_coche = None

        if ego_coche is not None:
            print('Datos - Se ha encontrado el vehiculo')
        else:
            print('ERROR - Datos - No se ha encontrado el vehiculo')

        blueprint_library = world.get_blueprint_library()

        # Camara central
        camera_bp = blueprint_library.find('sensor.camera.rgb')

        camera_bp.set_attribute('image_size_x', '640')
        camera_bp.set_attribute('image_size_y', '480')
        camera_bp.set_attribute('fov', '56')  # FOV 56 = PS Eye sin zoom
        #FOV 55 = Aukey

        camera_transform_central = carla.Transform(carla.Location(x=0.40, y=0.0, z=1.35))  # Respecto al parent
        camera = world.spawn_actor(camera_bp, camera_transform_central, attach_to=ego_coche)


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

        self.actor_list.append(camera)

        self.ego_coche = ego_coche
        



        self.sensors = [camera, camera_lateral1, camera_lateral2]


        # Thread
        t = threading.Thread(target=self._datosVision)
        t.daemon = True
        t.start()

        # Thread2
        t2 = threading.Thread(target=self._datosOBD)
        t2.daemon = True
        t2.start()


    def _datosOBD(self):
        while True:

            # Velocidad
            t = self.ego_coche.get_transform()
            v = self.ego_coche.get_velocity()
            a = self.ego_coche.get_acceleration()
            c = self.ego_coche.get_control()

            limite = self.ego_coche.get_speed_limit()

            self.velocidad = (3.6 * math.sqrt(v.x**2 + v.y**2 + v.z**2))
            self.acelerador = c.throttle
            self.freno = c.brake
            self.volante = c.steer
            self.limiteVelocidad = limite

            time.sleep(0.03)

    def _datosVision(self):
        def siempreUltimoFrame(imagen, q):
            if not q.empty():
                try:
                    q.get_nowait()  # descartamos ultimos frames
                except queue.Empty:
                    pass
            q.put(imagen)
            
        self.sensors[0].listen(lambda x: siempreUltimoFrame(x, self.q))
        self.sensors[1].listen(lambda x: siempreUltimoFrame(x, self.q1))
        self.sensors[2].listen(lambda x: siempreUltimoFrame(x, self.q2))



    def getDatosVision(self):
        return self.q.get(), self.q1.get(), self.q2.get()

    def getVelocidad(self):
        return self.velocidad

    def getAcelerador(self):
        return self.acelerador

    def getFreno(self):
        return self.freno
    
    def getVolante(self):
        return self.volante

    def read(self):
        return self.q.get(), self.q1.get(), self.q2.get()

    def desconectarDatosVision(self):
        print('Destruyendo actores', end='')
        for actor in self.actor_list:
            actor.destroy()
            print(".", end='')
        print('OK')

    def getLimiteVelocidad(self):
        return self.limiteVelocidad


class driverAttention:

    def __init__(self, ip='0.0.0.0', port=1234):
        
        self.q = queue.Queue()
        self.driverAttention = None

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))

        self.timerEntreBucles = None
        self.timerAux = None

        self.timerSinAtencion = 0.0

        # Thread
        t = threading.Thread(target=self._escuchaPuerto)
        t.daemon = True
        t.start()

        t2 = threading.Thread(target=self._timing)
        t2.daemon = True
        t2.start()


    def _timing(self):
            
        while True:
            time_inicial = time.time()
            timer = self.timerSinAtencion
            time.sleep(0.01)
            
            if self.driverAttention is None:
                pass
            elif not self.driverAttention:
                tiempobucle = time.time() - time_inicial
                timer = timer + tiempobucle
            else:
                timer = 0.0

            self.timerSinAtencion = timer

    
    def _escuchaPuerto(self):
        while True:
            timer_inicial = time.time()

            data, addr = self.sock.recvfrom(1024)
            if data:
                driverAttention = (data.decode("utf-8") == 'True')
                self.driverAttention = driverAttention



    def getDriverAttention(self):
        return self.driverAttention

    def getTimerAttention(self):
        return self.timerSinAtencion

    def desconecta(self):
        self.sock.close()
