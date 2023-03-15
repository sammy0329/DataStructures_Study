def ddd(N):
    A=[[1 for i in range(N)]]
    B=list(A[0])
    if(N==1):
        return [[1]]
    elif(N==2):
        return [[1,1],[2]]
    elif(N==3):
        return [[1,1,1],[2,1],[3]]
    while(True):
        B.pop()
        B.pop()
        B.insert(0,2)
        A.append(list(B))
        if(B.count(1) == 0 or B.count(1) == 1):
            break
    B=list(A[0])
    while(True):
        B.pop()
        B.pop()
        B.pop()
        B.insert(0,3)
        C=list(B)
        while(True):
            if(B.count(1) == 0 or B.count(1) == 1):
                break
            B.pop()
            B.pop()
            B.insert(0,2)
            A.append(list(B))
            if(B.count(1) == 0 or B.count(1) == 1):
                break
        B=list(C)
        if(B.count(1) == 0 or B.count(1) == 1 or B.count(1) == 2):
            break
    B=list(A[0])
    while(True):
        B.pop()
        B.pop()
        B.pop()
        B.insert(0,3)
        A.append(list(B))
        if(B.count(1) == 0 or B.count(1) == 1 or B.count(1) == 2):
            break
    return A


def factorial(M):
    facto = 1
    for i in range(1,M+1):
        facto = i*facto
    return facto


Num = int(input())
Number = [0 for i in range(Num)]
for i in range(Num):
    Number[i] = int(input())
for i in range(Num):
    answer = 0
    k=ddd(Number[i])
    for j in range(len(k)):
        answer=answer+factorial(len(k[j]))/(factorial(k[j].count(1))*factorial(k[j].count(2))*factorial(k[j].count(3)))
    
    print(int(answer))