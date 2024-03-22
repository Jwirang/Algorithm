import sys
n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
result= [0] * n
stack = []

for i in range(len(n_list)):
    while stack:
        if n_list[stack[-1][0]]<n_list[i]:
            stack.pop()
        else:
            result[i] = stack[-1][0]+1
            break
    stack.append((i,n_list[i]))
print(*result)