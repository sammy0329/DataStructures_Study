def solution(n, m, section):
    answer = 0

    while section:
        startIdx=section[0] # 맨앞에 있는 값 변수에 저장
        # startIdx부터 m개까지의 값들 중 section의 가장 앞에 있는 값에 해당하면 pop 작업
        for data in range(startIdx,startIdx+m):
            if section and data==section[0]: section.pop(0)
        # m번 만큼 칠했으므로 카운트해주기    
        answer+=1
    return answer

print(solution(8,4,[2, 3, 6]),2)
print(solution(5,4,[1, 3]),1)
print(solution(4,1,[1, 2, 3, 4]),4)
