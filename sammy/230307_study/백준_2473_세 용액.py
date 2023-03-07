import sys

input=sys.stdin.readline

n=int(input().rstrip())

dataList=list(map(int,input().rstrip().split()))

dataList.sort()

# 가장 큰 부분 세개를 골랐을 때의 절댓값을 result에 저장
result=abs(dataList[-1]+dataList[-2]+dataList[-3])
case=(dataList[0],dataList[1],dataList[2])

# 첫번째 값은 정해두고 나머지 두개를 선택하도록 진행
for target in range(n-2):
    start=target+1
    end=n-1
    
    while start<end:
        
         # dataList[start]와 dataList[end] 합을 check에 저장 후 절댓값과 result와 비교 후 갱신
        check=dataList[target]+dataList[start]+dataList[end]
        if result>=abs(check):
            result=abs(check)
            case=(dataList[target],dataList[start],dataList[end])
            
        # check 값이 음수이면 start+=1 , 양수이면 end-=1 진행 후 다시 이분탐색
        if check < 0:
            start+=1
            
        else:
            end-=1
print(*case)