def solution(n):
    answer=''

    while n:
        # 3으로 나눠떨어지지 않는 경우는 나머지를 answer에 넣어주고, 3으로 나눈 몫을 n에 저장 
        if n % 3:
            answer += str(n % 3)
            n //= 3
        
        # 3으로 나눠떨어지는 경우 4를 anwer에 넣어주고, 3으로 나눈 몫-1을 n에 저장
        else:
            answer += '4'
            n = n//3 - 1
  
    return answer[::-1] 

print(solution(1),1)
print(solution(2),2)
print(solution(3),4)
print(solution(4),11)
print(solution(10),41)
