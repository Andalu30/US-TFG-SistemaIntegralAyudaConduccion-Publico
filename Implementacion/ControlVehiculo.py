import carla



class ControlVehiculoSimulado:
    """ Wapper de comandos de Carla para control del vehículo
    """



    def __init__(self, ip, puerto=2000, coche="tesla.model3"):

        client = carla.Client(ip, puerto)
        client.set_timeout(2.0)

        world = client.get_world()
        self.world = world

        actores = world.get_actors()

        for actor in actores:
            if coche in actor.__str__():
                ego_coche = actor
                break
            else:
                ego_coche = None

        if ego_coche is not None:
            print('Control - Se ha encontrado el vehiculo')
        else:
            print('Control - No se ha encontrado el vehiculo')

        self.ego_coche = ego_coche
    
        self.volante = 0
        self.pedales = 0

    def modificaControlesVehiculo(self, volante, acelerador, freno):
        self.ego_coche.apply_control(carla.VehicleControl(throttle=acelerador, steer=volante, brake=freno))

    def modificaPosicionVolante(self, posicionVolante):
        self.ego_coche.apply_control(carla.VehicleControl(steer=posicionVolante))

    def modificaAcelerador(self, acelerador):
        print(f"enviando acelerador {acelerador}")
        self.ego_coche.apply_control(carla.VehicleControl(throttle=acelerador))

    def modificaFreno(self, freno):
        self.ego_coche.apply_control(carla.VehicleControl(brake=freno))

    def CarlaAutopilot(self, bool):
        try:
            self.ego_coche.set_autopilot(bool)
        except e:
            print(e)
