import random

# Number of nodes
n = 10
p = 0.5

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

def er_graph(g, p):
    '''
    Create a graph of the ER type
    :param g: graph of the type {1: [2,3], 2: [1,3], ..., n: [1,3]}
    :param p: probability of creating a link
    :return: g modified
    '''
    for i in g:
        for j in g:
            r = random.uniform(0, 1)
            if r > p:
                g[i].append(j)
    return g

g = create_graph(n)
g = er_graph(g, p)

print(g)