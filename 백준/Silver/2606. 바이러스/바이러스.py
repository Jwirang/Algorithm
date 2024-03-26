import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

count = 0
visit = [False] * (n + 1)
def dfs(node):
    global count
    visit[node] = True
    count += 1
    for i in graph[node]:
        if visit[i] == False:
            dfs(i)

dfs(1)
print(count - 1)