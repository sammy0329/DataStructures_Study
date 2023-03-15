import sys
 
def binary_search(start,end,M,charges): 
    result=0 # 이분탐색을 진행하며 만족하는 값을 저장해나갈 변수
    max_charge=max(charges)
    
    while start<=end: # 이분탐색 진행
        mid=(start+end)//2
        cnt=0
        money=0
        
        # 인출 가능 금액이 하루 charge 보다 작은 경우 start = mid + 1
        if mid < max_charge:
            start=mid+1
            continue
            
        for minus_money in charges: 
            # 하루 charge인 minus_money가 현재 들고 있는 money 보다 클 경우 인출
            if minus_money > money:
                cnt+=1
                money=mid
                
            money -= minus_money # 하루 charge 마이너스 처리

        # cnt가 M 보다 클 경우는 start 값을 키우기(start = mid + 1)    
        if cnt>M:
            start=mid+1 
            
        # cnt가 M 보다 작거나 같을 경우는 end 값을 줄이기(end = mid - 1)              
        else:
            result=mid
            end=mid-1          
                     
    return result

input=sys.stdin.readline

N,M=map(int,input().rstrip().split()) # N,M 입력 받기
charges = list(int(input()) for _ in range(N)) # 비용 입력받기
    
print(binary_search(min(charges),sum(charges),M,charges))