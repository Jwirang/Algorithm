import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)

def dfs(node):
    global count
    vistit[node] = True
    count += 1
    for i in graph[node]:
        if not vistit[i]:
            dfs(i)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

vistit = [False] * (n + 1)
count = 0
dfs(1)

print(count - 1)