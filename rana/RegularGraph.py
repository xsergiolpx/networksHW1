import random
import copy


def regular_graph(n, r):
    #print("Number of vertices must be greater than number of neighbours!")
    #print("Product of vertices and neighbours must be an even number")
    #n = int(input("Enter number of vertices: "))
    #r = int(input("Enter number of neighbours: "))

    s = 0

    myDict = {}
    count = {}

    x = []
    for a in range(1, n + 1):
        myDict[a] = copy.copy(x)
        count[a] = 0

    for i in range(1, r + 1):
        for j in range(1, n + 1):
            s = 0
            while s == 0:
                v = int(random.uniform(1, n + 1))
                if (v != j) and (v not in myDict[j]) and (count[v] < r):
                    myDict[j].append(v)
                    count[v] += 1
                    s = 1

    #print(count)
    return(myDict)
