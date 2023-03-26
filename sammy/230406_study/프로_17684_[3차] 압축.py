from string import ascii_uppercase
def solution(msg):
    answer = []
    data=dict()
    cnt=1
    for i in ascii_uppercase:
        data[i] = cnt
        cnt+=1
            
    check=msg[0]
    for idx in range(1,len(msg)):
        check+=msg[idx]
        if check not in data:
            data[check]=cnt
            cnt+=1
            answer.append(data[check[:-1]])
            check=check[-1]

    if check:
        answer.append(data[check])
            

    return answer

print(solution("KAKAO"),[11, 1, 27, 15])
print(solution("TOBEORNOTTOBEORTOBEORNOT"),[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution("ABABABABABABABAB"),[1, 2, 27, 29, 28, 31, 30])