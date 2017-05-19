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

    disconnected = []

    n = int(n)
    r = int(r)
    l = 0
    x = []
    for a in range(1, n + 1):
        myDict[a] = copy.copy(x)
        count[a] = 0
        disconnected.append(a)

    # print("disc")
    # print(disconnected)

    for i in range(1, r + 1):
        # print("********")
        for j in range(1, n + 1):
            s = 0
            l = 0
            # print("start...")
            while s == 0:
                v = int(random.uniform(1, n + 1))
                # print("v: ")
                # print(v)

                if (v != j) and (v not in myDict[j]) and (count[v] < r) and (count[j] < r):
                    # print("entered")
                    ##print(r)
                    # print(count[v])
                    if len(disconnected) == 1 and j == 1:
                        v = disconnected[0]

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
                    # print("else")

                l += 1
                # print(l)
                # print(myDict)

    return (myDict)


print(regular_graph(6, 5))
