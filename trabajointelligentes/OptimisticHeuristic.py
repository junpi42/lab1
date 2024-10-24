from trabajointelligentes.Heuristic import Heuristic, calculate_distance


class OptimisticHeuristic(Heuristic):
    def __init__(self, problem):
        self.problem = problem

    def g(self, node):
        return calculate_distance(self.problem.final_state, node.estado)

    def h(self, node):
        return calculate_distance(self.problem.initial_state, node.estado)