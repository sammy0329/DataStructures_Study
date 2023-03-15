count = 0
min_count=[] # 정답들 저장 리스트
checked_word=[] # 쓰인 단어 저장 리스트

def back(word,target,words):
    global count
    
    # 탐색하는 단어와 target이 일치할 때, count를 min_count에 저장 후 return
    if word==target: 
        # print(checked_word)
        min_count.append(count)
        return
    
    # 단어들 중 check해야 할 단어가 checked_word 리스트에 없을 때, 한 글자만 바꿀 수 있는지 체크 후 백트래킹 진행
    for check in words:
        # print((word,check),len(set(word)-set(check)))
        if check not in checked_word:
            cnt=0
            
            for idx in range(len(check)):
                if check[idx]!=word[idx]: cnt+=1                
            
            if cnt==1:  
                checked_word.append(check)
                count+=1
                back(check,target,words)
                checked_word.pop()
                count-=1
            

def solution(begin, target, words):    
    if target not in words: # 찾는 값이 words에 없으면 0 반환
        return 0
    
    back(begin,target,words) # 백트래킹 진행
    
    if min_count: # min_count 리스트에서 최솟값 반환
        return min(min_count)
    else: # min_count 리스트 값이 없다면 0 반환
        return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "dot", "hot"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
