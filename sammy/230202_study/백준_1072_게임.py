import sys

def binary_search(start,end,all,win): 
    result=-1 # 이분탐색을 진행하며 만족하는 값을 저장해나갈 변수
    percent=int(100*win/all) # 초기 승률 저장 변수
    new_percent=percent # 이분탐색을 진행하며 승률 초기화 해나갈 변수
    
    while start<=end: # 이분탐색 진행
        mid=(start+end)//2
        # new_percent는 이분탐색을 통해 더해나갈 mid 변수를 통해 연산 진행 후 초기화
        new_percent=int(100*(win+mid)/(all+mid))
        
        if new_percent<=percent: 
            start=mid+1 
           
        else:
            result=mid # 조건에 만족하면 mid를 result에 넣고 end=mid-1 진행
            end=mid-1
            
    return result


input=sys.stdin.readline().rstrip
all,win=map(int,input().split())

print(binary_search(0,all,all,win))

