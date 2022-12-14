from heapq import heappop,heappush

def cal(min1,min2):
    return min1+(min2*2)

def solution(scoville, K):
    answer = 0
    result=0
    heap=[]
    cnt=len(scoville)
    for num in scoville:
        heappush(heap,num)
    
    while cnt>=2:
        
        min1=heappop(heap)
        if min1>=K: return answer
        min2=heappop(heap)
        
        cnt-=2
        answer+=1
        result=cal(min1,min2)
        heappush(heap,result)
        cnt+=1

        if cnt<2 and result>=K: return answer
        # print(heap,result)

       

    return -1