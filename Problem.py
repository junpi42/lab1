import json

from clases import Action, State


class Problem:

    def __init__(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

        intersections = self.data['intersections']

        # diccionario para guardar los estados

        self.states = {}

        for intersection in intersections:  # esto es desde el primero hasta el final
            identificador = intersection['identifier']
            latitude = intersection['latitude']
            longitude = intersection['longitude']

            # ahora creamos un objeto del tipo State de la clase clases :)
            estado = State(latitude, longitude, identificador)

            self.states[identificador] = estado

        self.initial_state = self.states[self.data['initial']]
        self.final_state = self.states[self.data['final']]
        self.actions = {}

        for segment in self.data['segments']:
            id_origen = segment['origin']
            id_destino = segment['destination']
            distance = segment['distance']
            velocity = segment['speed']

            action = Action(id_origen, id_destino, distance, velocity)

            self.actions[(id_origen, id_destino)] = action

        # Creación del diccionario para guardar los posibles movimientos desde un punto

        self.grafo = {}

        for (id_origen, id_destino), action in self.actions.items():
            # Si ya tenemos el origen entonces no hace falta añadirlo otra vez,
            # solo añadimos otro destino más para ese origen
            if id_origen in self.grafo:
                self.grafo[id_origen].append(id_destino)  # .append es para añadir a la lista dentro del diccionario
            else:
                # Si no está, lo inicializamos con una lista que contiene el destino
                self.grafo[id_origen] = [id_destino]

    def is_final(self, p_state):
        return self.final_state == p_state
