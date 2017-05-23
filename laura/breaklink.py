from sergio.pergraph import *
from giusy.bfs import *
from laura.Throughput import *
from laura.ciao import *
from random import uniform
import matplotlib.pyplot as plt
#we write a function that remove links from the adjacency matrix of a graph, given the probability that a link can break down
def lb(a, p):
    '''
       :param a: adjacency matrix (nxn)
       :param p: probability of  a link break down
       :return: a modified
       '''
    for i in range(len(a)):
        for j in range(len(a)):
            r = uniform(0, 1)
            if a[i, j] == 1:
                if r < p:
                    a[i, j] = 0
                    a[j, i] = 0
    return a
#we write a function that converts an adjacency matrix(a) into a graph(dictionary)
def matrix_to_graph(a):
    g = {}
    for i in range(len(a)):
        g[i] =  []
        for j in range(len(a)):
              if a[i, j] == 1:
                     if i in g:
                         g[i].append(j)
                     else:
                         g[i] = [j]

    return g

th = []
th_er=[]
#we create graphs with the 2 networks model
g =regular_graph(20,8)
g_er=er_graph(p = 8/(20-1), n = 20)
#we construct the adjacency matrix
a_er=graph_to_matrix(g_er)
a = graph_to_matrix(g)
#Plot TH as a function of the probobility of a link brack down 
for i in np.arange(0 ,0.26,0.01):
    alb = lb(a , i)
    alb_er=lb(a_er,i)
    glb = matrix_to_graph(alb)
    glb_er=matrix_to_graph(alb_er)
    th.append(Throughput(glb))
    th_er.append(Throughput(glb_er))

plt.plot(th,label='regular')
plt.plot(th_er,label='p-Erdos-Renyi')
plt.legend( loc=2, borderaxespad=0.)
plt.show()

