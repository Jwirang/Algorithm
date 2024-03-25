import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)

def dfs(node, parent, graph):
    for child in graph[node]:
        if parent[child] == 0:
            parent[child] = node
            dfs(child, parent, graph)

n = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(n - 1):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

parent = {i: 0 for i in range(1, n + 1)}
dfs(1, parent, graph)

for i in range(2, n + 1):
    print(parent[i])