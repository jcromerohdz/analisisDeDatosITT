import networkx as nx
import matplotlib as plt
G = nx.Graph()
G.add_edges_from([(1,2),(1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node("spam")       # adds node "spam"
G.add_nodes_from("spam") # adds 4 nodes: 's', 'p', 'a', 'm'
G.number_of_edges()
G.number_of_nodes()
G.neighbors(1)  #vecinos de 1 o 2 o de otro nodo
G.remove_nodes_from("spam") # elimina todos los nodos de SPAM s,p,a,m
######### Atributos en los nodos ########
#G.clear()
G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
G.node[1]
#resultado#{'time': '5pm'}
G.node[1]['room'] = 714
G.nodes(data=True)#imprime los atributos
#resultado #[(1, {'room': 714, 'time': '5pm'}), (3, {'time': '2pm'})]


######### Atributos en los edges o enlaces ########
G.add_edge(1, 2, weight=4.7 )
G.add_edges_from([(3,4),(4,5)], color='red')
G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
G[1][2]['weight'] = 4.8
G.edge[1][2]['weight'] = 4
