#%%
import numpy as np

def solution(scores):
    answer = 1
    young = np.array(scores[0])
    scores = sorted(scores,key = lambda x : (x[0],x[1]))

    for i in range(len(scores)):
        
        scores[i] = np.array(scores[i])

    for i in range(len(scores)):##인센티브 못받는 놈들 제거 시간복잡도 N**2  
        
        cmp1 = scores[i]
        
        for j in range(len(scores)-1,i,-1):
            if(scores[j][0] == scores[i][0]):
                continue
                
            cmp2 = scores[j]
                
            if(cmp1<cmp2).all():
                scores[i] = np.array([-1,-1])
                break
    

    
    for i in range(len(scores)):
        if(scores[i] == np.array([-1,-1])).all():
            continue
        cmp = scores[i]
        
        if sum(cmp) > sum(young): ##석차 체크
            
            answer += 1
            
        if(young<cmp).all():
            
            return -1
    return answer

solution([[2,2],[1,4],[3,2],[3,2],[2,1]])
solution([[4, 1], [2, 4], [3, 5]]) #   2
