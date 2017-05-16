import numpy as np
from numpy import linalg as LA
def connectivityIrr(A):
    '''
        Check the connectivity of a graph 
        :param A: adjacency matrix (nxn)
        
        :return: True if The adjacency matrix is irreducible (the graph is connected), False if not
        '''
    I=np.identity(len(A))
    for i in range(1, len(A)):
       I+= LA.matrix_power(A,i)
    if (I>0).all():
        return True
        #print(' The adjacency matrix is irreducible,the graph is connected')
    else:
        return False
        #print(' The adjacency matrix is not irreducible,the graph is not connected')


