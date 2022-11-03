
str=list(input())
cursor=len(str)

n=int(input())

for _ in range(n):
    cmd=input().split()
    
    if cmd[0]=='L':
        if cursor>0:
            cursor-=1
    elif cmd[0]=='D':
        if cursor<len(str):
            cursor+=1
    elif cmd[0]=='B':
        if cursor>0:
            str.pop(cursor-1)
            cursor-=1
    elif cmd[0]=='P':
        str.insert(cursor,cmd[1])
        cursor+=1

for i in str:
    print(i,end='')
