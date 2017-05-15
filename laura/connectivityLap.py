from numpy import linalg as LA
import time
import numpy as np
def Degree(A):
   D = np.zeros((len(A), len(A)))
   for i in range(0,len(A)):
      D[i,i]=sum(A[i,:])
   return D

def connectivityLap(A):
    '''
           Check the connectivity of a graph 
           :param A: adjacency matrix (nxn)

           :return: True if The graph is connected, False if not
           '''
    D=Degree(A)
    L = D-A
    eigval = LA.eigvalsh(L)
    if eigval[1] > 0:
        return True
    else:
        return False
