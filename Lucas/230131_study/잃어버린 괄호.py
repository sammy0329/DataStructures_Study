#%%
from itertools import permutations
n = input("")
queue = []
check = []
answer = []
q = ""
for i in n:
    if(i == "-" or i == "+" or i == "*"):
        queue.append(int(q))
        queue.append(i)
        
        if(i not in check):
            check.append(i)
        q = ""
    else:
        q+=i
queue.append(int(q))

check = permutations(check,len(check))
test = queue.copy()
for i in check:
    queue = test.copy()
    for k in i:
        j = 0
        while True:
            j += 1
            if(j >=len(queue)):
                break
                
            if queue[j] == k:
                if(k == "+"):
                    queue[j] = queue[j-1] + queue[j+1]
                    queue.pop(j+1)
                    queue.pop(j-1)
                elif(k == "-"):
                    queue[j] = queue[j-1] - queue[j+1]
                    queue.pop(j+1)
                    queue.pop(j-1)
                j = 0
    answer.append(queue[0])

print(min(answer))
# %%
