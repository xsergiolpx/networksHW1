import random
import numpy as np

def create_graph(n):
    '''
    Creates a dictionary structure for n nodes {}
    :param n: number of nodes
    :return: something like {1: [2,3], 2: [1,3], ..., n: [1,3]}
    '''
    g = dict()
    for i in range(n):
        g[i] = []
    return g

def er_graph(p, n):
    '''
    Create a graph of the ER type
    :param g: graph of the type {1: [2,3], 2: [1,3], ..., n: [1,3]}
    :param p: probability of creating a link
    :return: g modified
    '''
    # create the nodes
    g = create_graph(n)
    for i in g:
        for j in g:
            if j > i:
                r = random.uniform(0, 1)
                if r < p:
                    g[i].append(j)
                    g[j].append(i)
    return g

def graph_to_matrix(g):

    '''
    Converts the graph g into a matrix m
    :param g: graph of the type {1: [2,3], 2: [1,3], ..., n: [1,3]}
    :return: m
    '''
    n = len(g)
    m = np.zeros((n, n))
    for i in g:
        l = g[i]
        for j in l:
            m[i,j] = 1
    return m


# Connect randomly the graph as ER
# g = er_graph(p = 0.5, n = 100)
