from sergio.pergraph import *
from laura.irreducibility import *
from sergio.conectivity_method_2 import *
from giusy.bfs import *
import numpy as np
import matplotlib.pyplot as plt
from rana.RegularGraph import *
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

N=100
prob=np.arange(0,1,0.01)
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

plt.loglog(prob, l, 'r-')
plt.show()
plt.plot(prob, l, 'r-')
plt.show()

'''
prob=np.arange(0,1,0.01)
l=[0.0, 0.0, 0.0, 0.01, 0.17, 0.53, 0.86, 0.94, 0.99, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
a=[0.0, 0.0, 0.0, 0.01, 0.12, 0.56, 0.86, 0.96, 0.99, 0.99, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

plt.loglog(prob, l, 'r-')
plt.axis([0,0.1, 0, 1])
plt.show()
print(np.mean(l[0:8]))
print(np.polyfit(prob,l, 2))
'''

###############  5.2   ##################
'''
N=10
n_values=np.arange(1,100,1)
r_values=[2,4,8,16]
l=[]
for n in n_values:
    for r in r_values:
        if n>r and (n*r%2)==0:
            print(n)
            con = 0
            for i in range(1,N+1):
                g=regular_graph(n=n,r=r)
                #m = graph_to_matrix(g)
                #L = matrix_L(g)
                c = bfs(g,1)
                if c==True:
                    con=con+1
            l.append(con/N)
'''
'''
n_values=np.arange(1,100,1)
r_values=[2,4,8,16]
for n in n_values:
    for r in r_values:
        if n>r and (n*r%2)==0:
            print(n,r)
            g = regular_graph(n=n, r=r)
            print(g)
            print("hola")
'''
#print(regular_graph(n=6, r=4))