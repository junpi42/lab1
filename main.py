from BestFirst import BestFirst
from BreadthFirst import BreadthFirst
from DepthFirst import DepthFirst
from Problem import Problem
from DepthLimitedSearch import DepthLimitedSearch
#----------------------------------- -------------------------------------------------------------
#ALGORITMO DE BUSQUEDA DEPTH-FIRST
#------------------------------------------------------------------------------------------------


problem = Problem(r"C://calle_agustina_aroca_albacete_500_1.json")


print("** ALGORITMO: Depth-First Search **")
depthFirst = DepthFirst(problem)
depthFirst.do_search()
print("\n----------------------------------------\n")

# Breadth-First Search
print("** ALGORITMO: Breadth-First Search **")
breadthFirst = BreadthFirst(problem)
breadthFirst.do_search()
print("\n----------------------------------------\n")

# Best-First Search
print("** ALGORITMO: Best-First Search **")
bestFirst = BestFirst(problem)
bestFirst.do_search()
print("\n----------------------------------------\n")

# Depth-Limited Search
print("** ALGORITMO: Depth-Limited Search **")
depthlimited = DepthLimitedSearch(problem, 28)
depthlimited.do_search()
print("\n----------------------------------------\n")

# Iterative Deepening Search
print("** ALGORITMO: Iterative Deepening Search **")
iterativeDeepening = IterativeDeepeningSearch(problem)
iterativeDeepening.do_search()
print("\n========================================\n")