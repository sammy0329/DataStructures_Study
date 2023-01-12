from itertools import permutations

N = int(input())

numbers = list(map(int,input().split(" ")))

m = list(map(int,input().split(" ")))
cal = []
for i in range(len(m)):
    if(i == 0):
        cal += ["+" for _ in range(m[i])]
    elif(i == 1):
        cal += ["-" for _ in range(m[i])]
    elif(i == 2):
        cal += ["*" for _ in range(m[i])]
    else:
        cal += ["/" for _ in range(m[i])]

allth = list(permutations(cal, sum(m)))
allth = list(set(allth))

min1 = "k"
max1 = "k"

for o in allth:
    num = 1
    ans = numbers[0]
    for i in o:

        if(i == "+"):
            ans = ans + numbers[num]
        elif(i == "-"):
            ans = ans - numbers[num]
        elif(i == "*"):
            ans = ans * numbers[num]
        else:
            if(ans<0):
                ans = -((-ans)//numbers[num])
            else:
                ans = ans // numbers[num]
        num+=1
    if(max1 == "k"):
        min1 = ans
        max1 = ans
    else:
        if(min1>ans):
            min1 = ans
        if(max1<ans):
            max1 = ans
print(max1)
print(min1)