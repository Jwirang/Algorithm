n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_result = float('-inf')
min_result = float('inf')

def dfs(depth, result):
    global max_result, min_result
    if depth == n - 1:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            new_result = calculate(result, arr[depth + 1], i)
            dfs(depth + 1, new_result)
            operator[i] += 1

def calculate(n1, n2, op):
    if op == 0: return n1 + n2
    elif op == 1: return n1 - n2
    elif op == 2: return n1 * n2
    elif op == 3: return int(n1 / n2)  # 정수 나눗셈으로 변경

dfs(0, arr[0])

print(max_result)
print(min_result)