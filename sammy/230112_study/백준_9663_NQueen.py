# 도전중
import sys

def backTracking(n,queencount,x,y):
    global count
    
    if queencount == n:
        count+=1
        return
    
    if x<0 or x>n or y<0 or y>n:
        return
    
    if visited[x][y]==True:
        visited[x][y]=False
        return
    
    if visited[x][y]==False:
        visited[x][y]=True
        nx,ny=0,0
        i=0
        while True:
            i+=1
            nx=x+dx[i]
            ny=y+dy[i]
                  
           
input = sys.stdin.readline
n=int(input())
visited=[[False]*n for _ in range(n)]
count=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

backTracking(n,0,0,0)
print(count)