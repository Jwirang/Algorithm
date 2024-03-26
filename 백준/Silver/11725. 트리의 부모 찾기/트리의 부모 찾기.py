import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)

def dfs(node):
    for i in graph[node]:
        if parent[i] == 0:
            parent[i] = node
            dfs(i)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])