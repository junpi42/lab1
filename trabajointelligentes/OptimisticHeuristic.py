from geopy.distance import geodesic

from trabajointelligentes.Heuristic import Heuristic


class OptimisticHeuristic(Heuristic):
    def __init__(self, problem):
        self.problem = problem

    def g(self, node):
        ini_lat = node.estado.latitude
        ini_lon = node.estado.longitude
        ini = (ini_lat, ini_lon)

        return geodesic(ini, (self.problem.final_state.latitude, self.problem.final_state.longitude)).km

    def h(self, node):
        return node.cost
