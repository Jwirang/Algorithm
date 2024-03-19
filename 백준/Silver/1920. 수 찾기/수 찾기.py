import sys
n = int(sys.stdin.readline())
n_list = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

for i in m_list:
    print('1') if i in n_list else print('0')