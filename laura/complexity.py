# 4 Compare the complexity as a function of n of the methods above
from sergio.pergraph import *
from laura.irreducibility import *
import time
import numpy as np
import matplotlib.pyplot as plt

#to compute the mean time  that the fuction to check the connectivity with the irreducibility algebraic method takes,depending on the number of nodes a a graph
tot = []
for i in range(2,61):
    g = er_graph(0.5, i)
    a = graph_to_matrix(g)
    times = []
    for j in range(301):
        start = time.time()
        connectivityIrr(a)
        end = time.time()
        times.append( end - start)
    tot.append(np.mean(times))

print(tot)
#to compute the mean time  that the fuction to check the connectivity with the laplacian algebraic method takes,depending on the number of nodes a a graph
totl=[]
for i in range(2,61):
    g = er_graph(0.5, i)
    L=matrix_L(g)
    times = []
    for j in range(301):
        start = time.time()
        eigenvalues_connected(L)
        end = time.time()
        times.append(end - start)
    totl.append( np.mean(times))

print(tot)

#to compute the mean time  that the fuction to check the connectivity with the breadth-rst search algorithm takes,depending on the number of nodes a a graph
totb=[]
for i in range(2,61):
    g = er_graph(0.5, i)
    times = []
    for j in range(301):
        start = time.time()
        bfs(g,np.random.randint(1,i))
        end = time.time()
        times.append(end - start)
    totb.append( np.mean(times))

print(totb)
plt.title('Comparison of the complexity of the functions to check the connectivity of a graph')
plt.ylabel('Execution time')
plt.xlabel('Number of nodes')
plt.plot(range(2,61),tot,label='Irreducibility algebraic method 2^O(n) exponential')
plt.plot(range(2,61),totl,label='Laplacian algebraic method O(log n)logarithmic')
plt.plot(range(2,61),totb,label='Breadth-rst search algorithm O(log n)logarithmic')
plt.legend( loc=2, borderaxespad=0.)

plt.show()







