from sergio.shortestpath import *

# g must be a dictionary containing nodes and edges between the nodes, the function will return Throughput/C
def Throughput(g):
    mat = []
    counter = 0
    maximum = 0
    n = len(g)

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                row = []
                row.append(i)
                row.append(j)
                paths = short_path(g, l=50, node1=i, node2=j)
                row.append(paths)
                row.append(len(paths))
                mat.append(row)

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                b = [i, j]
                l = 0.0
                for k in range(0, n):
                    found = 0
                    for m in range(0, len(mat[k][2])):
                        a = mat[k][2][m]
                        for p in range(len(a)):
                            if a[p:p + len(b)] == b:
                                found = 1
                                if mat[k][3] != 0:
                                  l = l + (1 / mat[k][3])

                mat[counter].append(l)
                counter += 1

                if l > maximum:
                    maximum = l
    if maximum != 0:
        return 1 / maximum
    else:
        return 1
#example
#a=er_graph(p = 8/10-1, n = 10)
#print(Throughput(a))