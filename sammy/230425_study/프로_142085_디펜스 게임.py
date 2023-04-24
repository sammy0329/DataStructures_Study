from heapq import heappush,heappop

def solution(n, k, enemy):
    heapq = []
    maxStage=0

    for stage,enemy_cnt in enumerate(enemy):
        heappush(heapq,-(enemy_cnt))
        n-=enemy_cnt
     
        maxStage+=1

        if n<0:
            if k<=0:
                return maxStage-1
            
            minus_k=0

            for i in range(k):
                minus_k+=1       
                pop_enemy_cnt=heappop(heapq)*-1
                n+=pop_enemy_cnt
                
                if n>=0:
                    k-=minus_k
                    break
                
            else:
                return maxStage-1
            
        

    return maxStage

print(solution(	7, 3, [4, 2, 4, 5, 3, 3, 1]),5)
print(solution(2, 4, [3, 3, 3, 3]),4)