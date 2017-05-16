from sergio.pergraph import *
from sergio.conectivity_method_2 import *
from laura.connectivityLap import *
from laura.irreducibility import *
g = er_graph(p = 0.5, n = 5 )

print(g)

def bfs(g,node):
    '''
    :param g: graph of the type {1: [2,3], 2: [1,3], ..., n: [1,3]}
    :param node: a given node from which I want to verify the connection
    :return: True if the graph is connected, False otherwise
    '''
    Q=[node]
    S=[]
    S.append(node)
    while len(Q)!=0:
        current=Q.pop()
        for i in g[current]:
            if i not in S:
                Q.append(i)
                S.append(i)
    if len(S)!=len(g):
        connection=False
    else:
        connection=True
    return(connection)


m=graph_to_matrix(g)
print(connectivityLap(m))
print(connectivityIrr(m))
print(bfs(g,4))
L = matrix_L(g)
print(eigenvalues_connected(L))
