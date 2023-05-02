def solution(targets):
    answer = 0
    targets.sort(key=lambda x : (x[1],x[0])) # end, start 순으로 sort 진행.
    end=0 # 현재 끝 지점 체크하기 위한 변수 지정
    
    for s,e in targets:
        if s>=end: # s가 현재 끝지점인 end 보다 크거나 같으면 answer에 1 더해주고, end 포인트를 e로 변경
            answer+=1
            end=e

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	), 3)

# 반례
print(solution([[0, 4], [1, 2], [1, 3], [3, 4]]),2)
print(solution([[0, 4], [0, 1], [2, 3]] ),2)