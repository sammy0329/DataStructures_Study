def solution(brown, yellow):
    answer = []
    total=brown+yellow # 두 격자의 총합
    
    for i in range(1, total+1):
        if total % i == 0: # i가 약수이면, 둘레의 길이가 brown인 값 찾기
            if (total//i)*2+(i-2)*2 == brown: # 둘레의 길이는 (total//i)*2+(i-2)*2
                answer=[total//i,i]   
                break 

    
    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))