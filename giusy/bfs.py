from sergio.pergraph import *
g = er_graph(p = 0.5, n = 5 )

print(g)

def bfs(g,node):
    Q=[node]
    S=[]
    S.append(node)
    while len(Q)!=0:
        current=Q.pop()
        for i in g[current]:
            if i not in S:
                Q.append(i)
                S.append(i)
    if len(S)!=len(g):
        connection=False
    else:
        connection=True
    return(connection)

print(bfs(g,4))