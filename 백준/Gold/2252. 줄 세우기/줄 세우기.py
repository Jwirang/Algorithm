import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    inDegree[b] += 1

q = deque()
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)
        
answer = []
while q:
    now = q.popleft()
    answer.append(now)
    for i in graph[now]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)

print(*answer)

