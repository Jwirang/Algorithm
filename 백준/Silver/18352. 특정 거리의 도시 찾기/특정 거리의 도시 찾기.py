import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()

    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)

if k in distance:
    for j in range(1, n+1):
        if distance[j] == k:
            print(j)
            check = True
else:
    print(-1)
