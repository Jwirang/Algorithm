import sys
import collections

n = int(sys.stdin.readline())
que = collections.deque([])

output = []
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        que.append(command[1])
    elif command[0] == 'front':
        if que:
            output.append(que[0])
        else:
            output.append(-1)
    elif command[0] == 'back':
        if que:
            output.append(que[-1])
        else:
            output.append(-1)
    elif command[0] == 'empty':
        if que:
            output.append(0)
        else:
            output.append(1)
    elif command[0] == 'pop':
        if que:
            output.append(que.popleft())
        else:
            output.append(-1)
    elif command[0] == 'size':
        output.append(len(que))

print('\n'.join(map(str, output)))
