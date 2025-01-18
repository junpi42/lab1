from abc import ABC, abstractmethod

from clases import Action, Node


class Search(ABC):
    def __init__(self, problem, depth_limit=None):
        self.problem = problem
        self.open_list = []
        self.explored = set()
        self.cost = 0
        self.NodesDictionary = {}
        self.TotalGenerated = 0
        self.ExpandedNodes = 0
        self.depth_limit = depth_limit  # Limite opcional de profundidad

    @abstractmethod
    def insert_node(self, node, node_list):
        pass

    @abstractmethod
    def extract_node(self, node_list):
        pass

    @abstractmethod
    def is_empty(self, node_list):
        pass

    def expand(self, current_state):
        ident = current_state.identificador
        sucesores = []

        if ident in self.problem.grafo:
            for idSucesores in self.problem.grafo[ident]:
                sucesor = self.problem.states[idSucesores]
                sucesores.append(sucesor)

        return sucesores

    def do_search(self):
        initial_node = Node(self.problem.initial_state, None, None)
        self.NodesDictionary[self.problem.initial_state] = initial_node
        self.insert_node(initial_node, self.open_list)
        self.TotalGenerated += 1

        while self.open_list:
            node = self.extract_node(self.open_list)
            if self.problem.is_final(node.estado):
                path = self.recover_path(node)  # Devolver el camino si se encuentra la solución
                print(f"Profundidad de la solución: {self.get_depth(node)}")
                return path

            if self.depth_limit is None or self.get_depth(node) < self.depth_limit:
                self.explored.add(node.estado.identificador)
                successors = self.expand(node.estado)
                self.ExpandedNodes += 1

                for successor in successors:
                    if successor.identificador not in self.explored:
                        new_action = Action(node.estado.identificador, successor.identificador, None, None)

                        if successor.identificador not in self.NodesDictionary:
                            new_node = Node(successor, new_action, node)
                            self.NodesDictionary[successor.identificador] = new_node
                        else:
                            new_node = self.NodesDictionary[successor.identificador]

                        self.insert_node(new_node, self.open_list)
                        self.TotalGenerated += 1

        print("No solution found")

    def get_depth(self, node: Node):
        depth = 0
        while node.parent is not None:
            depth += 1
            node = node.parent
        return depth

    def recover_path(self, node: Node):

        path = []

        while node is not None:
            path.append(node.estado)  # Añadir el identificador del estado actual
            node = node.parent  # Moverse al nodo padre

        # Imprimir el camino recorrido
        path.reverse()  # Invertir el camino para mostrar de inicio a fin
        for i, estado in enumerate(path):
            print(f"{i}: {estado}")

        # Imprimir el número total de estados
        print(f"El número total de estados es: {len(path)}")
        print(f"Total de nodos generados: {self.TotalGenerated}")
        print(f"Total de nodos expandidos: {self.ExpandedNodes}")
        self.NodesDictionary.clear()  # vaciamos el diccionario por si el programa no para de ejecutarse y buscamos otra cosa
        return path
