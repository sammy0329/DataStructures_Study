import sys
N=int(sys.stdin.readline())
stack=[]
for _ in range(N):
    data=list(map(str,sys.stdin.readline().split()))
    print(data)
    if data[0]=='push':
        stack.append(int(data[1]))
        
    elif data[0]=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif data[0]=='size':
        print(len(stack))
        
    elif data[0]=='empty':
        if stack:
            print(0)
        else:
            print(1)
            
    elif data[0]=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    