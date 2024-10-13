import json
from clases import State,Action,Node

with open(r'C:\\calle_agustina_aroca_albacete_250_0.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

intersections =data['intersections']



#diccionario = {}

states = {}

for intersection in intersections:#esto es desde el primero hasta el final
    identificador = intersection['identifier']
    latitude = intersection['latitude']
    longitude = intersection['longitude']

    #ahora creamos un objeto del tipo State de la clase clases :)
    estado= State(latitude,longitude,identificador)

    states[identificador]= estado

actions={}

for segment in data['segments']: #otra forma de hacer un for diciendo desde 
    id_origen = segment['origin']
    id_destino = segment['destination']
    distance= segment['distance']
    velocity= segment['speed']

    accion = Action(id_origen,id_destino,distance,velocity)

    actions[(id_origen,id_destino)]=accion


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
def expand(current_state):  
    ident = current_state.identificador  
    sucesores = []

    if ident in grafo:
        for idSucesores in grafo[ident]:
            sucesor = states[idSucesores]
            sucesores.append(sucesor)

    return sucesores
        
def recover_path(node: Node):
    path = []

    while node is not None:
        path.append(node.estado.identificador)  # Añadir el identificador del estado actual
        # Si node.parent es None, entonces hemos llegado al nodo raíz (el inicial)
        if node.parent is None:
            break
        node = Node(states[node.parent], None, node.parent)

    # Imprimir el camino recorrido
  
    for estado in path:
        print(f"{estado} + ")

    # Imprimir el número total de estados
    print(f"El número total de estados es: {len(path)}")
    
    return path 
    

def depth_first_search(initial_state, goal_state):
    open_list = [Node(initial_state, None,None)]
    explored = set()

    while open_list :  # Aquí se comprueba si la lista no está vacía ||||| conforme avanza el algoritmo se nos quedara algo asi  ( 2,3,4,5,8,9)
        
        
        node = open_list.pop() #el pop coge y elimnina el ultimo nodo de esta lista
        
        if node.estado.identificador == goal_state.identificador: #una vez llega aqui comprueba si el nodo en el que estamos es el que queremos al final
             recover_path(node)   #~si son iguales devuelve el camino hasta llegar aqui
             return
            
        explored.add(node.estado.identificador)   #si no son iguales añade el nodo actual a la lista de explorados para no volver a el 
        successors= expand(node.estado)
        
        print (successors)
        for successor in successors: #sacamos los sucesores de la funcion expand que usa el diccionario grafos y itera sobre cada uno de los sucesores
            if successor.identificador not in explored:   #comprobamos que no esta explorado
                accionNuevo= Action(node.estado.identificador,successor.identificador,None,None)
                new_node = Node(successor,accionNuevo,node.estado.identificador)     #si no esta explorado ,lo añadimos a la lista open_list para comenzar el bucle de nuevo
                open_list.append(new_node)
    
    
    print("NO HAY SOLUCIONES")
    
    

initial_id = data['initial']  
goal_id = data['final']        
initial_state_obj = states[initial_id]  
goal_state_obj = states[goal_id]        

depth_first_search(initial_state_obj, goal_state_obj) 