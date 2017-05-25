from sergio.pergraph import *
from laura.irreducibility import *
from sergio.conectivity_method_2 import *

from giusy.bfs import *
import numpy as np
import matplotlib.pyplot as plt
from giusy.modified import *
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

###############  5.2   ##################
'''
N=100
n_values=np.arange(1,101,1)
r_values=[4]
t=[]
l=[]
for n in n_values:
    con = 0
    for r in r_values:
        if n>r and (n*r%2)==0:
            print(n)
            for i in range(1,N+1):
                g=regular_graph(n=n,r=r)
                #m = graph_to_matrix(g)
                #L = matrix_L(g)
                c = bfs(g,1)
                if c==True:
                    con=con+1
    l.append(con/N)
print(l)
print(len(l))
prob=np.arange(0,1,0.01)
plt.plot(n_values, l, 'r-')
plt.axis([0, 100, -0.1, 1.1])
plt.show()
'''

'''

N=10
l=[]
n_values=np.arange(1,101,1)
r_values=[2,4,8,16]
for n in n_values:
    for r in r_values:
        con = 0
        if n>r and (n*r%2)==0:
            for i in range(1, N + 1):
                print(n,r)
                g = regular_graph(n=n, r=r)
                bfs(g,1)
                if c == True:
                    con = con + 1
    print(con)
    l.append(con / N)

print(l)
'''
'''
l=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
print(len(l)/4)
prob=np.arange(0,1,0.01)
r2=len(l[0:99])


#print(regular_graph(n=6, r=4))
'''

N=100
n_values=np.arange(1,101,1)
r_values=[2,4,8,16]
l=[]
for r in r_values:
    for n in n_values:
        con = 0
        if n>r and (n*r%2)==0:
            print(n)
            for i in range(1,N+1):
                g=regular_graph(n=n,r=r)
                #m = graph_to_matrix(g)
                #L = matrix_L(g)
                c = bfs(g,1)
                if c==True:
                    con=con+10
        l.append(con/N)
print(l)
n_values=np.arange(1,101,1)
a=l[0:100]
b=l[100:200]
c=l[200:300]
plt.plot(n_values, a)
plt.plot(n_values, b)
plt.plot(n_values, c)

plt.axis([0, 100, -0.1, 1.1])
plt.show()

'''
import numpy as np
l=[0.0, 0.0, 1.0, 1.0, 1.0, 0.9, 0.6, 0.6, 0.8, 0.8, 0.7, 0.8, 0.8, 0.5, 0.4, 0.2, 0.2, 0.5, 0.2, 0.2, 0.5, 0.3, 0.2, 0.7, 0.5, 0.3, 0.6, 0.6, 0.4, 0.0, 0.0, 0.3, 0.2, 0.2, 0.0, 0.2, 0.3, 0.2, 0.2, 0.3, 0.3, 0.3, 0.4, 0.1, 0.8, 0.3, 0.4, 0.2, 0.4, 0.3, 0.4, 0.3, 0.1, 0.1, 0.3, 0.3, 0.2, 0.2, 0.1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.2, 0.5, 0.1, 0.4, 0.3, 0.1, 0.3, 0.3, 0.1, 0.2, 0.3, 0.2, 0.2, 0.1, 0.4, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.1, 0.2, 0.4, 0.0, 0.2, 0.2, 0.3, 0.1, 0.3, 0.3, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
n_values=np.arange(1,101,1)
print(len(l))
a=l[0:100]
b=l[100:200]
y = [a,b]
print(len(y))
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("A test graph")
plt.plot(n_values,a)
plt.plot(n_values,b)
plt.show()
'''
