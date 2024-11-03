class Action:
    def __init__(self, origin, destination, distance, velocity):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.velocity = velocity

    def __eq__(self, other):
        if isinstance(other, Action):
            return (self.origin == other.origin and self.destination == other.destination
                    and self.distance == other.distance)
        return False

    def __repr__(self):
        return f"Action({self.origin}, {self.destination}, {self.distance})"

    def __str__(self):
        return f"\nOrigin:  + {self.origin} + \nDestiny:  + {self.destination} + \nCost:  + {self.distance}"

    def time(self):
        return self.distance/self.velocity

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
    Esta es una clase padre que contiene las otras 2
    """

    def __init__(self, estado, action, parent=None, cost=0, time=0):
        self.estado = estado
        self.action = action
        self.parent = parent
        self.cost = cost + time

    def __eq__(self, id2):
        if isinstance(id2, Node):
            return self.estado.__eq__(id2.estado) and self.parent.__eq__(id2.parent) and self.action.__eq__(
                id2.action)
        return False

    def __repr__(self):
        return f"Action({self.estado}, {self.parent}, {self.action})"

    def __str__(self):
        return f"\nOrigin:  + {self.action} + \nDestiny:  + {self.parent} + \nCost:  + {self.action}"
