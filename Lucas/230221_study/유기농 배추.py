import sys
sys.setrecursionlimit(10000)

def ccc(x,y):
    
    global M
    global N
    
    if(check[y][x]==True):
        return 0
    
    check[y][x] = True
    
    if(y+1<=N-1 and arr[y+1][x]==1):
        ccc(x,y+1)
    if(y-1>=0 and arr[y-1][x]==1):
        ccc(x,y-1)
    if(x+1<=M-1 and arr[y][x+1]==1):
        ccc(x+1,y)
    if(x-1>=0 and arr[y][x-1]==1):
        ccc(x-1,y)
    
    return 1



T = int(input())
answer= [0 for c in range(T)]

for c in range(T):
    M,N,K = map(int,input().split())
    
    location = []
    check = [[False for i in range(M)] for i in range(N)]
    arr =[[0 for i in range(M)] for i in range(N)]
    
    for i in range(K):
        X,Y = map(int,input().split())
        arr[Y][X] = 1
        location.append([X,Y])


    for i in location:
        answer[c]+=ccc(i[0],i[1])
        
        
for c in range(T):
    print(answer[c])