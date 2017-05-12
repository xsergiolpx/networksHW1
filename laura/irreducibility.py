from sergio.pergraph import *
def connectivityIrr(A):
   #type A: (adjacency)matrix

    for i in range(0, len(A)):
       I=sum(A**i) #I+=A**i
    if I>0:
        return True
        #print(' The adjacency matrix is irreducible,the graph is connected')
    else:
        return False
        #print(' The adjacency matrix is not irreducible,the graph is not connected')


def connectivityLap(A):
    L=(1/2)*A.transpose()*A
