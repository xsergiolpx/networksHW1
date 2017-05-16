# create the D matrix
from pergraph import *

def matrix_d(g):
    '''
    Given a graph g return the matrix D
    :param g:  graph of the type {1: [2,3], 2: [1,3], ..., n: [1,3]}
    :return: the matrix D
    '''
    n = len(g)
    m = np.zeros((n, n))
    for i in g:
        m[i,i] = len(g[i])
    return m

def matrix_L(g):
    '''
    Create the L = D - G matrix
    :param g:
    :return:
    '''
    return (matrix_d(g)-graph_to_matrix(g))

def eigenvalues_connected(L):
    '''
    Checks if the second eigenvalue of L is positive and therefore connected (True) or not connected (False)
    :param L:
    :return: True if connected or False if not connected
    '''
    eigenvalues = np.linalg.eigvals(L)
    second_smallest = sorted(eigenvalues)[1]
    if second_smallest > 0:
        return True
    else:
        return False



'''
#Example:
#Create a graph
g = er_graph(p=0.5, n=5)

#Get the matrix L

L = matrix_L(g)

#Print the graph and if it is connected or not
print(g)
print(eigenvalues_connected(L))

'''

