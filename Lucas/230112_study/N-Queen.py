#%%
from itertools import combinations

n = int(input())
answer = 0
coords = []
maps = [[0 for _ in range(n)] for i in range(n)]
for x in range(len(maps)):
    for y in range(len(maps[x])):
        print((x,y))
        coords.append((x,y))

result = list(combinations(coords, n))
print(result)
#%%
def check(locations):
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i == j:
                continue
            if locations[i][0] == locations[i][0]:
                return 0
            if locations[i][1] == locations[i][1]:
                return 0
            if abs(locations[i][0]-locations[j][0]) == abs(locations[i][1]-locations[j][2]):
                return 0

    return 1

for i in result:

    answer += check(i)

#%%
print(answer)
# %%
