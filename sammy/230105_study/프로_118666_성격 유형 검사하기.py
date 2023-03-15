def solution(survey, choices):
    answer = ''
    
    # 점수 저장할 딕셔너리 생성
    data={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    # survey, choices 리스트를 활용해 점수 처리
    for idx,check in enumerate(survey):
        if choices[idx]>4:
            data[check[1]]+=choices[idx]-4
        elif choices[idx]<4:
            data[check[0]]+=(-choices[idx])+4
    
    
    # 리스트로 해당 딕셔너리 값들을 받음
    test=list(data.items())
    
    
    # 성격 유형 처리
    for i in range(0,8,2):
        if test[i][1] >= test[i+1][1]: answer+=test[i][0]
        elif test[i][1] < test[i+1][1]: answer+=test[i+1][0]
        
    return answer


# print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
# print(solution(["TR", "RT", "TR"],[7, 1, 3]))