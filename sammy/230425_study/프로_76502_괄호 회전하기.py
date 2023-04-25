def solution(s):
    answer = 0
    check=s

    for _ in range(len(s)):
        # 괄호 하나씩 뒤에 붙이기
        check_=check[1:]+check[0]
        # 변경시킨 check_를 check에 반영
        check=check_
        
        for _ in range(len(s)//2): # s 길이의 2로 나눈만큼 (),{},[] replace 진행하여 ""로 만들어주기
            check_=check_.replace('()','')
            check_=check_.replace('{}','')
            check_=check_.replace('[]','')

        if check_=="": # "" 갯수 카운팅
            answer+=1

    return answer

print(solution("[](){}"),3)
print(solution("}]()[{"),2)
print(solution(	"[)(]"),0)
print(solution("}}}"),0)
