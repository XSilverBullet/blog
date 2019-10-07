import collections
import sys

# record topologic sort result
res = []

'''
N: Number of graph
prerequisites: list<int, int>
'''


def canFinish(prerequisites):
    graph = collections.defaultdict(list)
    indegrees = collections.defaultdict(int)
    for u, v in prerequisites:
        graph[v].append(u)
        indegrees[u] += 1

    # val 0 of indegree added into
    Q = [u for u in graph.keys() if indegrees[u] == 0]

    while Q:
        #pop from front of queue
        u = Q.pop()

        res.append(u)
        for v in graph[u]:
            indegrees[v] -= 1

            if indegrees[v] == 0:
                Q.append(v)

    for idx in range(len(indegrees)):
        if not (indegrees[idx]==0):
            return False

    return True


a = []
for line in sys.stdin:
    tempStr = [int(a) for a in line.split()]
    a.append(tempStr)

b = []
for i in range(len(a)):
    if len(a[i]) >= 2:
        for j in range(1, len(a[i])):
            b.append([a[i][0], a[i][j]])
print(b)
if canFinish(b):
    print(res)
else:
    print(-1)
