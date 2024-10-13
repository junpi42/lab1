


class Action:
    def __init__(self,origin,destination,distance,velocity):
        self.origin=origin
        self.destination=destination
        self.distance=distance
        self.velocity=velocity

class State:
    """
    Esta clase guarda la posición de nuestro nodo en latitud y longitud
    """
    def __init__(self, latitude, longitude, identificador):
        self.latitude = latitude
        self.longitude = longitude
        self.identificador = identificador

    def __str__(self):
        return f"State(id: {self.identificador}, lat: {self.latitude}, lon: {self.longitude})"
        
    def __repr__(self):
        return self.__str__() 
class Node:
    """
    esta es una clase padre que contiene las otras 2
    """
    def __init__(self,estado,action,parent,):
        self.estado=estado
        self.action=action
        self.parent=parent
        

