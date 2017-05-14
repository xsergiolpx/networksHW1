from numpy import linalg as LA

def connectivityLap(A):
    L=(1/2)*A.transpose()*A
    eigval= LA.eigvalsh(A)
    if eigval[1]>0:
        return True
    else :
        return False
