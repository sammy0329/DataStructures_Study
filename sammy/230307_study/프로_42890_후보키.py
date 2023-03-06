from itertools import combinations

def solution(relation):
    candidates=[] # 유일성 만족시키는 후보군
    answer = [] # 유일성과 후보군 모두 만족시키는 정답
    combies=[] # 만들 수 있는 조합

    # 만들 수 있는 모든 조합들 combies에 저장
    for i in range(1,len(relation[0])+1):
        combies.extend(combinations(range(len(relation[0])),i))
    
    # 유일성
    for combi in combies:
        # 2차원 리스트는 set으로 변환 안되므로 tuple 활용
        check_cols = [tuple(row[col] for col in combi) for row in relation]
        # 중복 제거한 리스트 길이가 relation의 행의 길이와 같다면 구분 가능하다는 것
        if len(set(check_cols))==len(relation):
            candidates.append(set(combi))

    # 최소성
    for idx,req in enumerate(candidates):
        for check in answer:
            # issubset 함수를 활용하여 부분집합인지 파악
            if check.issubset(req):
                break
        # for문이 도는 동안 break 걸리지 않았다면 유일성, 최소성 모두 만족하므로 answer에 저장
        else: answer.append(req)
                
    
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]),2)