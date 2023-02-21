def yaksu(n):
    cnt=0
    # n의 제곱근까지의 약수 구하기
    for i in range(1,int(n**0.5)+1):
        # 나눠 떨어지면 cnt+1
        if n%i == 0:
            cnt+=1
            # 제곱했을 때 n이 되면 짝이 없는 것, n이 아니면 짝이 있으므로 cnt+1
            if i**2 != n:
                cnt+=1
    return cnt
            
def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        yaksu_cnt=yaksu(i)
        # 약수 개수가 limit를 넘으면 power을 더해주고, 그 외에는 약수 개수 더해주기 
        if yaksu_cnt>limit:
            answer+=power
        else:
            answer+=yaksu_cnt
    return answer

# print(solution(5,3,2))
# print(solution(10,3,2))