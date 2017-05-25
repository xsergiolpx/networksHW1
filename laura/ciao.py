import random
import copy


def checkCount(dic, r, x):
    if dic[x] != (r):
        return False
    else:
        return True


def finalCheck(dic, n, r):
    for p in range(0, n):
        if dic[p] != (r):
            return False
    return True


def regular_graph(n, r):
    s = 0

    myDict = {}
    count = {}

    disconnected = []

    n = int(n)  # nodes
    r = int(r)  # edges
    l = 0
    found = 0
    done = 0
    x = []

    while found != 1:

        l = 0
        myDict.clear()
        count.clear()
        disconnected[:] = []
        done = 0

        for a in range(0, n):
            myDict[a] = copy.copy(x)
            count[a] = 0
            disconnected.append(a)

        for i in range(0, r):
            for j in range(0, n):
                s = 0
                l = 0
                change = 0

                while s == 0 and l != (n * r):
                    v = int(random.uniform(0, n))

                    if (v != j) and (v not in myDict[j]) and (count[v] < r) and (count[j] < r):

                        if len(disconnected) == 1 and done == 0 and disconnected[0] != j:
                            v = disconnected[0]
                            done = 1

                        myDict[j].append(v)
                        myDict[v].append(j)
                        count[v] += 1
                        count[j] += 1

                        if v in disconnected:
                            disconnected.remove(v)
                        if j in disconnected:
                            disconnected.remove(j)

                        s = 1

                    elif (checkCount(count, r, j)):
                        s = 1

                    prev = myDict
                    l += 1

        if finalCheck(count, n, r):
            found = 1

    return (myDict)

r=regular_graph(10,2)
print(r)