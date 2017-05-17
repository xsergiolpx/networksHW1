from sergio.pergraph import *
from laura.irreducibility import *
from sergio.conectivity_method_2 import *
from giusy.bfs import *
import numpy as np
import matplotlib.pyplot as plt
'''
-creare un grafo con n=100 facendo variare il parametro p [0,1]
-generare N grafi (es: N=50) e calcolare la proporzione di grafi connessi su N
'''

'''
N=5
prob=np.arange(0,1,0.01)
l=[]
for p in prob:
    con = 0
    for i in range(1,N+1):
        g=er_graph(p = p, n = 100 )
        m = graph_to_matrix(g)
        c=connectivityIrr(m)
        if c==True:
            con=con+1
    l.append(con/N)
    print(p)
print(l)

plt.plot(prob, l, 'ro')
plt.show()
'''
N=100
prob=np.arange(0,1,0.1)
l=[]
for p in prob:
    con = 0
    for i in range(1,N+1):
        g=er_graph(p = p, n = 100 )
        #m = graph_to_matrix(g)
        L = matrix_L(g)
        c = eigenvalues_connected(L)
        if c==True:
            con=con+1
    l.append(con/N)
    print(p)
    print(l)

plt.plot(prob, l, 'ro')
plt.show()