###########################################
##### 2.3 Reliability performance #########
###########################################
from sergio.pergraph import *
from rana.RegularGraph import *
from rana.Throughput import *
from random import uniform
import matplotlib.pyplot as plt
import numpy


def meanz(*a):
    sums = []
    sm = 0

    for i in range(len(a[0][0])):
        sm = 0
        for j in range(len(a[0])):
            sm = sm + a[0][j][i]
        sums.append(sm)

    for k in range(len(sums)):
        sums[k] = sums[k] / len(a[0])
    return sums

def means(*a):
    arr = numpy.array(a)
    arr = numpy.mean(arr, axis=1)
    return arr[0]

def standDev(*a):
    arr = numpy.array(a)
    arr = numpy.std(arr, axis=1)
    return arr[0]


# we write a function that remove links from the adjacency matrix of a graph, given the probability that a link can break down
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


# we write a function that converts an adjacency matrix(a) into a graph(dictionary)
def matrix_to_graph(a):
    g = {}
    for i in range(len(a)):
        g[i] = []
        for j in range(len(a)):
            if a[i, j] == 1:
                if i in g:
                    g[i].append(j)
                else:
                    g[i] = [j]

    return g



fin_th = []
fin_er = []
find_th = [] #to store standard deviation
find_er = [] #to store standard deviation
finm_th = [] #to store mean
finm_er = [] #to store mean
# we create graphs with the 2 networks model
for k in range(0, 15):
    g = regular_graph(20, 8)
    g_er = er_graph(p=8 / (20 - 1), n=20)
    # we construct the adjacency matrix
    a_er = graph_to_matrix(g_er)
    a = graph_to_matrix(g)
    tot_th = []
    tot_er = []
    # Plot TH as a function of the probobility of a link brack down
    for i in np.arange(0, 0.26, 0.02):
        alb = lb(a, i)
        alb_er = lb(a_er, i)
        glb = matrix_to_graph(alb)
        glb_er = matrix_to_graph(alb_er)
        th = []
        th_er = []
        for j in range(300):
            th.append(Throughput(glb))
            th_er.append(Throughput(glb_er))
        tot_th.append(np.mean(th))
        tot_er.append(np.mean(th_er))

    fin_th.append(tot_th)
    fin_er.append(tot_er)

finm_th = means(fin_th)
finm_er = means(fin_er)

find_th = standDev(fin_th)
find_er = standDev(fin_er)


print(finm_th)
print(find_th)

std=find_th*2/np.sqrt(15)
std_er=find_er*2/np.sqrt(15)

fig=plt.figure()
plt.title('Reliability performance: TH as a function of p')
plt.ylabel('Throughput Performance')
plt.xlabel('Probability that a link can break down in a r-regular graph')
prob = np.arange(0, 0.26, 0.02)
plt.plot(prob, finm_th+std, label='lim-sup')
plt.plot(prob, finm_th, label='r -regular random graph')
plt.plot(prob, finm_th-std, label='lim-inf')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
fig.savefig("Reliability_performance1.png")

fig=plt.figure()
plt.title('Reliability performance: TH as a function of p')
plt.ylabel('Throughput Performance')
plt.xlabel('Probability that a link can break down in a er-graph')
plt.plot(prob, finm_er+std_er, label='lim-sup')
plt.plot(prob, finm_er, label='p-ER random graph')
plt.plot(prob, finm_er-std_er, label='lim-inf')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
fig.savefig("Reliability_performance2.png")
