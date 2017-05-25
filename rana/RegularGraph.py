import random
import copy


def checkCount(dic, r, x):
    if dic[x] != (r):
        return False
    else:
        return True


def regular_graph(n, r):
    s = 0

    myDict = {}
    count = {}

    n = int(n)
    r = int(r)

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
                    myDict[v].append(j)
                    count[v] += 1
                    count[j] += 1
                    s = 1
                elif (checkCount(count, r, j)):
                    s = 1

    return (myDict)


print(regular_graph(n=4, r=2))