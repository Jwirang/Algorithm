import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

visit = [False] * (n+1)

def dfs(v):
    visit[v] = True
    for i in graph[v]:
        if visit[i] == False:
            visit[i] == True
            dfs(i)
count = 0
for i in range(1, n+1):
    if visit[i] == False:
        count += 1
        dfs(i)
print(count)
