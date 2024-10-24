from abc import abstractmethod, ABC
from math import radians, sin, cos, sqrt, atan2

from trabajointelligentes.clases import State


def calculate_distance(state_a: State, state_b: State):
    # Convert latitude and longitude from degrees to radians
    lat1 = radians(state_a.latitude)
    lon1 = radians(state_a.longitude)
    lat2 = radians(state_b.latitude)
    lon2 = radians(state_b.longitude)

    # Haversine formula to calculate the distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radius of Earth in kilometers. Use 3956 for miles
    radius_of_earth_km = 6371.0

    # Calculate the distance
    distance = radius_of_earth_km * c

    return distance


class Heuristic(ABC):
    @abstractmethod
    def h(self, node):
        pass

    @abstractmethod
    def g(self, node):
        pass
