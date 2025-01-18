from asyncio import PriorityQueue

from OptimisticHeuristic import OptimisticHeuristic
from Search import Search


class BestFirst(Search):
    def __init__(self, problem):
        Search.__init__(self, problem)
        self.heuristic = OptimisticHeuristic(problem)
        self.node_queue = PriorityQueue()
        self.id = 0

    def insert_node(self, node, node_list):
        self.node_queue.put_nowait((self.heuristic.g(node), self.id, node))
        self.id += 1
        node_list.append(node)

    def extract_node(self, node_list):
        node_list.pop(0)
        return self.node_queue.get_nowait()[2]

    def is_empty(self, node_list):
        return self.node_queue.empty()