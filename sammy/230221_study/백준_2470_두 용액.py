import sys

input = sys.stdin.readline
n = int(input().rstrip())

# 산성 용액과 알칼리성 용액의 특성값 입력 후 정렬
data=list(map(int,input().split()))
data.sort()

# 처음과 끝 포인터 지정
start=0
end=n-1

# 처음 data[start]와 data[end] 합의 절댓값을 임의 result에 저장
# case에 각각 data[start]와 data[end] 저장
result=abs(data[start]+data[end])
case=(data[start],data[end])

# 이분탐색 시작
while start<end:
    # data[start]와 data[end] 합의 절댓값을 check에 저장 후 result와 비교 후 갱신
    check=data[start]+data[end]
    
    if result>=abs(check):
        result=abs(check)
        case=(data[start],data[end])
        
    # check 값이 음수이면 start+=1 , 양수이면 end-=1 진행 후 다시 이분탐색
    if check < 0:
        start+=1
        
    else:
        end-=1
print(case[0],case[1])