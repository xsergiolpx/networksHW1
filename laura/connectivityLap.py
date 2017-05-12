from numpy import linalg as LA, sort

def connectivityLap(A):
    L=(1/2)*A.transpose()*A
    eigval= sort(LA.eigvalsh(A))
    if eigval[1]>0:
        return True
    else :
        return False
