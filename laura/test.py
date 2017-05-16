#from sergio.pergraph import *
#from laura.connectivityLap import *
#from laura.irreducibility import *
from numpy import linalg as LA
import time


g = er_graph(p = 0.5, n = 100)
a=graph_to_matrix(g)
start=time.time()
connectivityIrr(a)
end=time.time()
tot = end - start
print(tot)
startl = time.time()
connectivityLap(a)
endl = time.time()
totl = endl - startl
print(totl)



