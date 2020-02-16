import random


def createGraph(p = 0.02, n = 1000):
    result = []
    for i in range(1, n):
         for j in range(i + 1, n + 1):
            if random.random() <= p:
                result.append([i,j])
    trueSet = {}
    for i in range(1,n+1):
        trueSet[i] = [];
    for i in result:
        trueSet[i[0]].append(i[1])
        trueSet[i[1]].append(i[0])
    return trueSet
