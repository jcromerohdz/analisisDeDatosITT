import networkx as nx
import matplotlib as plt
G = nx.Graph()
G.add_node(11)
G.add_nodes_from([22,33])#agrega nodos desde una lista
#nx.path_graph()  genera una red con los elementos y con edges
H = nx.path_graph(10)
#H.nodes() 
# imprime los nodos de H
#H.edges() 
#imprime los enlaces en H
#nx.draw(H) 
# grafica los nodos y enlaces en H sin etiquetar
#nx.draw(H,with_labels = True)
# grafica los nodos y enlaces con etiquetas
G.add_nodes_from(H) 
# agrega solo nos nodos en H
G.add_edge(1,2) # agregar manualmente los enlaces
e=(2,3) #tupla
G.add_edge(*e) # unpack edge tuple*
G.add_edges_from([(1,2),(1,3)])# agregar varios enlaces
#agregar nodos desde otro grafo
G.add_edges_from(H.edges())
#nx.draw(H,with_labels = True)
#G.remove_node(H)
#
#G.clear() #elimina todos los nodos