#%%
maps = []
a = 1
rows = 6
col = 7
for i in range(rows):
    maps.append([i for i in range(a,a+col)])
    a += col
#%%
print(maps)
# %%
x1,y1,x2,y2 = 2,2,5,4
nx,ny = x1,y1
a = maps[ny][nx]
r = (x2-x1)
c = (y2-y1)
for i in range(((x2-x1) + (y2-y1))*2):
    if(i<r-1):
        nx += 1
    elif(r-1<=i<r+c):
        ny += 1
    elif(r+c<=i<r+r+c-1):
        nx -= 1
    elif(r+r+c-1<=i<r+r+c+c):
        ny -= 1
    print(nx,ny)
# %%
def solution(rows, columns, queries):
    maps = []
    a = 1
    answer = []
    for i in range(rows):
        maps.append([i for i in range(a,a+columns)])
        a += columns
    
    for i in queries:
        min1 = []
        y1,x1,y2,x2 = i
        nx,ny = x1,y1
        a = maps[ny-1][nx-1]
        r = (x2-x1)
        c = (y2-y1)
        for i in range((r+c+2)*2-4):
            if(i<r):
                nx += 1

            elif(r<=i<r+c):
                ny += 1

            elif(r+c<=i<r+r+c):
                nx -= 1

            elif(r+r+c<=i<r+r+c+c):
                ny -= 1

            min1.append(a)
            b = maps[ny-1][nx-1]
            maps[ny-1][nx-1] = a
            a = b
        answer.append(min(min1))
    
    return answer
#%%
solution(100,97,[[1,1,100,97]])
# %%
