import matplotlib.pyplot as plt
import networkx as nx

n=10
g=er_graph(0.5,n)
sp= short_path(g, 2, 0, n-1):
print(sp)

a=graph_to_matrix(g)
G=nx.from_numpy_matrix(np.array(a))
pos=nx.spring_layout(G)
plt.show()
nx.draw(G,pos,node_color="yellow",with_labels=True)
path=nx.shortest_path(G,source=0,target=n-1)
path_edges=zip(path,path[1:])
nx.draw_networkx_nodes(G,pos,nodelist=path,node_color="r")
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color="r",width=10)
plt.axis('equal')
plt.show()
