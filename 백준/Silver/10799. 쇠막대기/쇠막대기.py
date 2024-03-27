import sys 
n = sys.stdin.readline().strip('\n')
stack=0
cnt=0
for i in range(len(n)):
    if n[i]=='(':
        stack+=1
        cnt+=1
    elif n[i-1]=='(':
        stack-=1
        cnt-=1
        cnt+=stack
    else:
        stack-=1

print(cnt)