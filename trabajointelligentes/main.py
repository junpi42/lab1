import json
from clases import State,Action
from dfs import DepthFirstSearch

with open(r'C:\\calle_agustina_aroca_albacete_250_0.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

intersections =data['intersections']



#diccionario para guardar los estados

states = {}

for intersection in intersections:#esto es desde el primero hasta el final
    identificador = intersection['identifier']
    latitude = intersection['latitude']
    longitude = intersection['longitude']

    #ahora creamos un objeto del tipo State de la clase clases :)
    estado= State(latitude,longitude,identificador)

    states[identificador]= estado


#Diccionario para las acciones

actions={}

for segment in data['segments']: 
    id_origen = segment['origin']
    id_destino = segment['destination']
    distance= segment['distance']
    velocity= segment['speed']

    accion = Action(id_origen,id_destino,distance,velocity)

    actions[(id_origen,id_destino)]=accion



#Creaccion del diccionario para guardar los posibles movimientos desde un punto

grafo = {}

for (id_origen, id_destino), action in actions.items():
    # Si ya tenemos el origen entonces no hace falta añadirlo otra vez, solo añadimos otro destino mas para ese origen
    if id_origen in grafo:
        grafo[id_origen].append(id_destino) # .append es para añadir a la lista dentro del diccionario
    else:
        # Si no está, lo inicializamos con una lista que contiene el destino
        grafo[id_origen] = [id_destino]



#------------------------------------------------------------------------------------------------
#ALGORITMO DE BUSQUEDA DEPTH-FIRST
#------------------------------------------------------------------------------------------------

    

initial_id = data['initial']  
goal_id = data['final']        
initial_state = states[initial_id]  
goal_state = states[goal_id]        

dfs_instance = DepthFirstSearch(grafo, states) #creamos una instancia
dfs_instance.search(initial_state, goal_state)
