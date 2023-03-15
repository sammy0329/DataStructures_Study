dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
       'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def solution(s):
    answer = ''  # 결괏값 넣을 문자열
    check = ''  # 문자 판단할 문자열

    for i in s:
        # try except를 통해 int로 형변환시 예외가 발생하면 문자열이라 판단하고 check에 더해나간다.
        # 만약 미리 정의해둔 딕셔너리 안에 문자가 확인되면 결괏값에 더해나간다
        try:
            if check in dic:
                answer += str(dic[check])
                check = ''
            data = int(i)
            answer += i
        except:
            check += i

    if check in dic:
        answer += str(dic[check])

    return int(answer)

# print(solution("one4seveneight"),1478)
# print(solution("23four5six7"),234567)
# print(solution("2three45sixseven"),234567)
# print(solution("123"),123)
