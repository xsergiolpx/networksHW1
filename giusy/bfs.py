from sergio.pergraph import *
g = er_graph(p = 0.5, n = 10)
print(g)

def bfs(g,node):
    Q=[]
    Q.append(node)
    
