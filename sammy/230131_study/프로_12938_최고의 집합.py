def solution(n, s):
    answer = []
    if n>s: return [-1] # n이 s보다 크면 만들 수 있는 경우의 수가 없음.
    
    mid=s//n # s를 n으로 나눈 몫을 mid 변수에 저장
    last=s%n # 나머지를 last 변수에 저장
    
    # answer에 mid 값을 n개 만큼 저장
    for i in range(n):
        answer.append(mid)
    
    # idx에 마지막 인덱스 값 저장
    idx=n-1
    
    # last 값이 0이 안될때 까지 각각의 인덱스를 -1 해가며 해당 값에 1을 더해주고, last 또한 -1 해준다.
    while last:
        answer[idx]=answer[idx]+1
        idx-=1
        last-=1
       
    return answer


# print(solution(2,9))
# print(solution(2,1))
# print(solution(2,8))