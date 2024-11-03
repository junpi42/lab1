from trabajointelligentes.BestFirst import BestFirst
from trabajointelligentes.DepthFirst import DepthFirst
from trabajointelligentes.Problem import Problem
from trabajointelligentes.assets.AStar import AStar

#------------------------------------------------------------------------------------------------
#ALGORITMO DE BUSQUEDA DEPTH-FIRST
#------------------------------------------------------------------------------------------------


problem = Problem("assets/problems/calle_agustina_aroca_albacete_5000_0.json")

# depthFirst = DepthFirst(problem)
# depthFirst.do_search()

#------------------------------------------------------------------------------------------------
#ALGORITMO DE BUSQUEDA DEPTH-FIRST
#------------------------------------------------------------------------------------------------

# breadthFirst = BreadthFirst(problem)
# breadthFirst.do_search()

#------------------------------------------------------------------------------------------------
#ALGORITMO DE BUSQUEDA BEST-FIRST
#------------------------------------------------------------------------------------------------

bestFirst = AStar(problem)
bestFirst.do_search()
