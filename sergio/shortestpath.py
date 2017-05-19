from sergio.dijkstra import *
from sergio.pergraph import *
import copy

# Delete nodes
def delete_nodes(gd, path):
    '''
    Deletes the intermidiete nodes in the path from the weighted graph
    :param gd: weighted graph
    :param path: path output in list form
    :return: gd modified without the nodes
    '''
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


def delete_link(gd, node1, node2):
    del(gd[node1][node2])
    del(gd[node2][node1])
    return gd
# Convert g to the format of the library used
def convert_to_dij(g):
    '''
    Conver the graph g to a graph that is weigthed
    :param g: graph
    :return:
    '''
    dic = {}
    for node in g:
        dic[node] = {node2: 1 for node2 in g[node]}

    return dic

def dif_size(caminos, path):
    if path is False:
        return True
    if len(caminos) is 0:
        size = 1000
    else:
        size = len(caminos[0])
    if size < len(path):
        return True
    else:
        return False


def short_path(g, l, node1, node2):
    gd = convert_to_dij(g)
    caminos = []
    coun = 0
    while 1:
        path = shortestPath(gd, node1, node2)
        #print(path)
        # Pop the nodes
        if path is not False and dif_size(caminos, path) is False:
            caminos.append(path[:])
            coun = coun + 1
            if len(path) > 2:
                #if the path has more than 2 nodes (node1 and node2) then remove them
                gd = delete_nodes(gd, path)
            else:
                # This is when the link from node1 to node 2 is direct and we must remove
                # it so the program works
                delete_link(gd, node1, node2)

        if path is False or coun is l or dif_size(caminos, path) is True:
            # No more paths or we found l shortest paths
            return caminos

'''
# how to use it:
# first create a graph, for example a ER-graph with the parameters recomended
n = 100
p = 8/(n-1)
g = er_graph(p=p, n=n)

# Now to find the l paths run with your desired parameters this:
paths = short_path(g, l=4, node1=0, node2=n-1)

# Where g is the graph generated from er_graph(), l is the maximum number of shortest paths,
# node1 is the node from the begining and node2 is the end node
# Now we print the paths, and gives a list of lists (paths)
# i.e from 0 to 99 we can get this result: [[0, 27, 12, 99], [0, 20, 16, 99], [0, 70, 23, 99], [0, 68, 47, 99]]

print(paths)

# If we set l = 4 but there are only 3 disjoint paths, the output will be a list of 3 lists
'''

