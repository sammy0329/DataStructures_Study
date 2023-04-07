from string import ascii_uppercase

def solution(msg):
    answer = []
    data=dict()
    cnt=1
    for i in ascii_uppercase: # 대문자를 key로 하고 인덱스를 value로 하여 딕셔너리에 추가
        data[i] = cnt
        cnt+=1
            
    check=msg[0] # 첫 문자를 check에 넣기
    for idx in range(1,len(msg)):
        check+=msg[idx] # check에 문자 하나씩 붙여넣기
        if check not in data: # 딕셔너리에 없으면 추가하고 마지막 문자를 제외한 check[:-1] value 값을 answer에 append 후, check는 마지막 문자만 남겨두기
            data[check]=cnt
            cnt+=1
            answer.append(data[check[:-1]])
            check=check[-1]

    if check: # for문이 끝나고 남은 check 값 처리
        answer.append(data[check])
            
    return answer

print(solution("KAKAO"),[11, 1, 27, 15])
print(solution("TOBEORNOTTOBEORTOBEORNOT"),[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution("ABABABABABABABAB"),[1, 2, 27, 29, 28, 31, 30])