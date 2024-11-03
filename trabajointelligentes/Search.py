from abc import ABC, abstractmethod

from trabajointelligentes.clases import Action, Node


class Search(ABC):
    def __init__(self, problem):
        self.problem = problem
        self.open_list = None
        self.explored = set()
        self.cost = 0
        self.NodesDictionary = {}

    @abstractmethod
    def insert_node(self, node, node_list):
        pass

    @abstractmethod
    def extract_node(self, node_list):
        pass

    @abstractmethod
    def is_empty(self):
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

        while not self.is_empty():
            node = self.extract_node(self.open_list)
            if self.problem.is_final(node.estado):
                path = self.recover_path(node)  # Devolver el camino si se encuentra la solución
                return path

            self.explored.add(node.estado.identificador)
            successors = self.expand(node.estado)

            for successor in successors:
                if successor.identificador not in self.explored:
                    new_action = self.problem.actions[(node.estado.identificador, successor.identificador)]
#                    new_action = Action(node.estado.identificador, successor.identificador, None, None)

                    if successor.identificador not in self.NodesDictionary:
                        new_node = Node(successor, new_action, node, node.cost, new_action.time())
                        self.NodesDictionary[successor.identificador] = new_node
                    else:
                        new_node = self.NodesDictionary[successor.identificador]

                    self.insert_node(new_node, self.open_list)

        print("No solution found")

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
        self.NodesDictionary.clear()  # vaciamos el diccionario por si el programa no para de ejecutarse y buscamos otra cosa
        return path
