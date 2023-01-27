from math import inf
from collections import defaultdict

# 인접행렬을 지정하라.
W = [[0, 32, inf, 17, inf, inf, inf, inf, inf, inf], #1
     [32, 0, inf, inf, 45, inf, inf, inf, inf, inf], #2
     [inf, inf, 0, 18, inf, inf, 5, inf, inf, inf], #3
     [17, inf, 18, 0, 10, inf, inf, 3, inf, inf], #4
     [inf, 45, inf, 10, 0, 28, inf, inf, 25, inf],  #5
     [inf, inf, inf, inf, 28, 0, inf, inf, inf, 6], #6
     [inf, inf, 5, inf, inf, inf, 0, 59, inf, inf], #7
     [inf, inf, inf, 3, inf, inf, 59, 0, 4, inf], #8
     [inf, inf, inf, inf, 25, inf, inf, 4, 0, 12], #9
     [inf, inf, inf, inf, inf, 6, inf, inf, 12,   0]] #10

def prim(W):
    V = len(W)
    F = defaultdict(list)

    nearest = [0] * V
    distance = [W[0][i] for i in range(V)]
    distance[0] = -1

    for _ in range(V-1):
        min = inf
        for i in range(1, V):
            if (0 < distance[i] < min):
                min = distance[i]
                vnear = i

        F[nearest[vnear]].append(vnear)
        distance[vnear] = -1

        for i in range(1, V):
            if W[i][vnear] < distance[i]:
                distance[i] = W[i][vnear]
                nearest[i] = vnear
    return F

assert prim(W) == defaultdict(list, {0: [3, 1], 3: [7, 4, 2], 7: [8], 8: [9], 9: [5], 2: [6]})