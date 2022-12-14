def solution(citations):
    answer = 0
    citations.sort() # citations 오름차순 정렬
    n=len(citations) 
    
    # 이진 탐색을 위한 start, end 값 지정
    start=0 
    end=citations[-1]
    
    while(start<=end):
        mid=(start+end)//2
        
        # 배열 앞에서 부터 mid 보다 큰 값 탐색 후, 찾으면 index에 저장 후, break
        for idx in range(len(citations)):
            if citations[idx]>=mid: 
                index=idx
                break
        
        # n-index는 mid번 이상 인용된 논문 수
        # index는 나머지    
        
        # mid가 n-index 즉, n편 중 mid번 이상 인용된 논문이 mid 이하일 때,
        # 그리고 그 외 나머지 즉, index가 mid 번 이상일 때 end를 mid-1로 줄임
        if n-index<mid or index>mid:
            end=mid-1
        else: # 문제 조건에 맞을 경우 최댓값을 구해야하므로 answer에 저장하고 start를 늘려 계속 구해본다.
            answer=mid
            start=mid+1
    
    return answer





solution([3, 0, 6, 1, 5])