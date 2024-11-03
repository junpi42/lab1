from abc import abstractmethod, ABC
from math import radians, sin, cos, sqrt, atan2

from trabajointelligentes.clases import State

class Heuristic(ABC):
    @abstractmethod
    def h(self, node):
        pass

    @abstractmethod
    def g(self, node):
        pass
