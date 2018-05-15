# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ea = search.GPSProblem('E', 'A', search.romania)
ld = search.GPSProblem('L', 'D', search.romania)



#print search.breadth_first_graph_search(ab).path()
#print search.depth_first_graph_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()
print "Camino  de B a A"
print search.ramificacion_y_salto(ab).path()
print search.ramificacion_y_salto_con_acot(ab).path(), "\n"

print "Camino  de A a E"
print search.ramificacion_y_salto(ea).path()
print search.ramificacion_y_salto_con_acot(ea).path(), "\n"

print "Camino  de D a L"
print search.ramificacion_y_salto(ld).path()
print search.ramificacion_y_salto_con_acot(ld).path(), "\n"


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
