#from sergio.pergraph import *
import numpy as np
def connectivityIrr(A):
    '''
        Check the connectivity of a graph 
        :param A: adjacency matrix (nxn)
        
        :return: True if The adjacency matrix is irreducible (the graph is connected), False if not
        '''
    I=np.identity(len(A))
    for i in range(0, len(A)):
       I+=A**i
    if (I>0).all():
        return True
        #print(' The adjacency matrix is irreducible,the graph is connected')
    else:
        return False
        #print(' The adjacency matrix is not irreducible,the graph is not connected')

