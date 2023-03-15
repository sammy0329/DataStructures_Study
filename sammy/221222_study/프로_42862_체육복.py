# 전체 학생 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reverse

def solution(n, lost, reserve):
    # set으로 중복값 처리
    answer=0
    new_reserve = list(set(reserve) - set(lost))
    new_lost = list(set(lost) - set(reserve))
    
    # reserve의 +-1 값 check_lost와 비교.
    for check_reserve in new_reserve: 
       
        front = check_reserve - 1
        back = check_reserve + 1

        if front in new_lost:
            new_lost.remove(front)
            
        elif back in new_lost:
            new_lost.remove(back)

    # n에서 new_lost 뺀 값이 answer        
    answer=n - len(new_lost)

    return answer
    

# print(solution(5,[2,4],[1, 3, 5]))
# print(solution(5, [2, 4], [3]))