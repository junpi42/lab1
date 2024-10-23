from trabajointelligentes.BestFirst import BestFirst
from trabajointelligentes.BreadthFirst import BreadthFirst
from trabajointelligentes.DepthFirst import DepthFirst
from trabajointelligentes.Problem import Problem

#------------------------------------------------------------------------------------------------
#ALGORITMO DE BUSQUEDA DEPTH-FIRST
#------------------------------------------------------------------------------------------------


problem = Problem("assets/problems/small/avenida_de_espanÌa_250_0.json")

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

bestFirst = BestFirst(problem)
bestFirst.do_search()
