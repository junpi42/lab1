from clases import Action, Node


# ------------------------------------------------------------------------------------------------
# ALGORITMO DE BUSQUEDA DEPTH-FIRST
# ------------------------------------------------------------------------------------------------


class BreadthFirstSearch:
    def __init__(self, grafo, states):
        self.grafo = grafo  # Grafo que contiene los caminos entre nodos
        self.states = states  # Diccionario de estados
        self.NodesDictionary = {}  # Diccionario de nodos creados

    def expand(self, current_state):  # metodo para expandir los nodos

        ident = current_state.identificador
        sucesores = []

        if ident in self.grafo:
            for idSucesores in self.grafo[ident]:
                sucesor = self.states[idSucesores]
                sucesores.append(sucesor)

        return sucesores

    def recover_path(self, node: Node):

        path = []

        while node is not None:
            path.append(node.estado.identificador)  # Añadir el identificador del estado actual
            node = node.parent  # Moverse al nodo padre

        # Imprimir el camino recorrido
        path.reverse()  # Invertir el camino para mostrar de inicio a fin
        for i, estado in enumerate(path):
            print(f"{i}: {estado}")

        # Imprimir el número total de estados
        print(f"El número total de estados es: {len(path)}")
        self.NodesDictionary.clear()  # vaciamos el diccionario por si el programa no para de ejecutarse y buscamos otra cosa
        return path

    def search(self, initial_state, goal_state):

        open_list = []

        # Crear el nodo inicial y almacenarlo en el diccionario
        initial_node = Node(initial_state, None, None)
        self.NodesDictionary[initial_state.identificador] = initial_node
        open_list.append(initial_node)

        explored = set()

        while open_list:
            node = open_list.pop(0)
            print(node.estado.identificador)

            if node.estado.identificador == goal_state.identificador:
                self.recover_path(node)  # Devolver el camino si se encuentra la solución
                return None

            explored.add(node.estado.identificador)
            successors = self.expand(node.estado)

            for successor in successors:
                if successor.identificador not in explored:
                    accionNuevo = Action(node.estado.identificador, successor.identificador, None, None)

                    if successor.identificador not in self.NodesDictionary:
                        new_node = Node(successor, accionNuevo, node)
                        self.NodesDictionary[successor.identificador] = new_node
                    else:
                        new_node = self.NodesDictionary[successor.identificador]

                    open_list.append(new_node)

        print("NO HAY SOLUCIONES")
        return None

