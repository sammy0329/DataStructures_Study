n,m=list(map(int,input().split(' ')))
arr=list(map(int,input().split()))

start=0
end=max(arr)

result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    
    for x in arr:
        if x>mid:
            total+=x-mid
            
    # 떡의 양이 부족한 경우 왼쪽 부분 탐색        
    if total<m:
        end=mid-1
        
    # 떡의 양이 충분한경우 오른쪽 부분 탐색  
    else:
        result=mid
        start=mid+1
print(result)
