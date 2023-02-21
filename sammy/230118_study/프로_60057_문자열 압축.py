def solution(s):
    s_len=len(s) # s의 길이 저장
    answer = s_len
    
    for i in range(1,s_len//2+1):
        data='' # 압축된 문자 저장
        cnt=1
        check=s[:i]
        
        for j in range(i,s_len,i):
            # check와 값이 같으면 cnt 증가
            if check==s[j:j+i]: 
                cnt+=1
                
            else:
                # cnt가 2보다 크거나 같으면 data에 압축 값 삽입
                if cnt>=2: data+=str(cnt)+check 
                else: data+=check
                
                # check를 다시 초기화
                check=s[j:j+i]          
                cnt=1
        
        # 남은 문자열 처리   
        if cnt>=2: data+=str(cnt)+check 
        else: data+=check

        # answer 보다 작으면 최신화
        if answer>len(data): answer=len(data)
        
    return answer


# print(solution("aabbaccc")) # 7
# print(solution("ababcdcdababcdcd")) # 9
# print(solution("abcabcdede")) # 8
# print(solution("abcabcabcabcdededededede")) # 14
# print(solution("xababcdcdababcdcd")) # 17
