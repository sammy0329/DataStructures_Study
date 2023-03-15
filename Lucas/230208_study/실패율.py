def solution(N, stages):
    answer = []
    di = []
    for i in range(1,N+1):
        lose = 0
        total = 0
        
        for j in stages:
            if j >= i:
                total+=1
            if j == i:
                lose+=1
        if(total == 0):
            di.append((0,i))
        else:
            di.append((lose/total,i))
                  
    di = sorted(di,key = lambda x : (x[0], -x[1]),reverse = True)
    for i in di:
        answer.append(i[1])
    return answer
