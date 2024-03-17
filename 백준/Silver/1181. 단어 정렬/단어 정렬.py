import sys
n = int(sys.stdin.readline())
data = [str(sys.stdin.readline().strip()) for i in range(n)]

data.sort()
data.sort(key=len)
world = []

for x in data:
    if x not in world:
        world.append(x)

for i in world:
    print(i)