from asyncio import PriorityQueue

from trabajointelligentes.OptimisticHeuristic import OptimisticHeuristic
from trabajointelligentes.Search import Search


class BestFirst(Search):
    def __init__(self, problem):
        Search.__init__(self, problem)
        self.heuristic = OptimisticHeuristic(problem)
        self.open_list = PriorityQueue()
        self.id = 0

    def insert_node(self, node, node_list):
        self.open_list.put_nowait((self.heuristic.g(node), self.id, node))
        self.id += 1

    def extract_node(self, node_list):
        return self.open_list.get_nowait()[2]

    def is_empty(self):
        return self.open_list.empty()