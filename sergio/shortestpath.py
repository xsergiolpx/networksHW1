from sergio.dijkstra import *
from sergio.pergraph import *
import copy

# Delete nodes
def delete_nodes(gd, path):
    gd_copy = dict.copy(gd)
    delete_this = path[1:-1]
    # Delete the nodes
    for node in gd:
        if node in delete_this:
            del(gd_copy[node])

    # Update the original gd
    del(gd)
    gd = dict.copy(gd_copy)

    # Delete the edges
    for node in list(gd):
        for link in list(gd[node]):
            if link in delete_this:
                del(gd_copy[node][link])

    return gd_copy

# Convert g to the format of the library used
def convert_to_dij(g):
    dic = {}
    for node in g:
        dic[node] = {node2: 1 for node2 in g[node]}

    return dic


def short_path(g, l, node1, node2):
    gd = convert_to_dij(g)
    caminos = []
    coun = 0
    while 1:
        path = shortestPath(gd, node1, node2)
        print(path)
        # Pop the nodes
        if path is not False:
            caminos.append(path[:])
            coun = coun + 1
            gd = delete_nodes(gd, path)

        if path is False or coun is l:
            # No more paths or we found l shortest paths
            return caminos



n = 10
p = 8/(n-1)

g = {0: [3, 6, 7, 9], 1: [8], 2: [], 3: [0, 5, 7], 4: [5], 5: [3, 4, 6], 6: [0, 5, 9], 7: [0, 3], 8: [1], 9: [0, 6]}#er_graph(p=0.2, n=n)
print(g)
paths = short_path(g, l=4, node1=0, node2=9)

print(paths)
