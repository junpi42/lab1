


class Action:
    def __init__(self,origin,destination,distance,velocity):
        self.origin=origin
        self.destination=destination
        self.distance=distance
        self.velocity=velocity

class State:
    """
    esta clase guarda la posicion de nuestro nodo en latitud y longitud
    """
    def __init__(self,latitude,longitude,identificador):
        self.latitude=latitude
        self.longitude=longitude
        self.identificador=identificador
    def __str__(self):
        return (f'state with id: {self.identificador}')

        
class Node:
    """
    esta es una clase padre que contiene las otras 2
    """
    def __init__(self,estado,action,parent,):
        self.estado=estado
        self.action=action
        self.parent=parent
        

