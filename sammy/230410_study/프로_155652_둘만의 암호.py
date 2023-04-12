def solution(s, skip, index):
    answer = ''

    for i in s:
        cnt=0 # 변환 가능 횟수 카운팅
        check=ord(i) # 초기 아스키코드값

        while True:
            check+=1 # 두의 알파벳으로 변경

            if check>122: # 'z'를 넘어가면 'a'로 초기화
                check=97
                
            if chr(check) not in skip: # skip에 해당 문자가 없다면 cnt 카운팅
                cnt+=1
                if cnt==index: # 인덱스만큼 돌았으면 answer에 해당 문자를 붙여주기
                    answer+=chr(check)
                    break

    return answer

print(solution("aukks","wbqd",5),"happy")