import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visit = [False] * (n + 1)
def dfs(node):
    visit[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if visit[i] == False:
            dfs(i)

visited = [False] * (n + 1)           
def bfs(node):
    q = deque([node])
    visited[node] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
            


dfs(v)
print()
bfs(v)