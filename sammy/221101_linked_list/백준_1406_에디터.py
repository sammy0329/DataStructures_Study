
left=list(input())


n=int(input())
right=[]

for _ in range(n):
    cmd=input().split()
    if cmd[0]=='L':
        if left:
            right.append(left.pop())
            # print(left,right)
    elif cmd[0]=='D':
        if right:
            left.append(right.pop())
            # print(left,right)
    elif cmd[0]=='B':
        if left:
            left.pop()
            # print(left,right)
    elif cmd[0]=='P':
        left.append(cmd[1])
        # print(left,right)       
left.extend(reversed(right))
for i in left:
    print(i,end='')