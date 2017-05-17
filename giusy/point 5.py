from sergio.pergraph import *
from laura.irreducibility import *
from sergio.conectivity_method_2 import *
from rana.RegularGraph import *
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
###############  5.1   ##################
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
'''
###############  5.2   ##################

N=5
r_values=[2,4,8,16]
n_values=np.arange(2,100,1)
l=[]
for r in r_values:
    for n in n_values:
        con = 0
        for i in range(1,N+1):
            if n>r and (n*r%2==0):
                g=regular_graph(n,r)
                #m = graph_to_matrix(g)
                #L = matrix_L(g)
                c = bfs(g,1)
                if c==True:
                    con=con+1
        l.append(con/N)
        print(r)
        print(n)

print(l)
#plt.plot(n_values, l, 'ro')
#plt.show()


