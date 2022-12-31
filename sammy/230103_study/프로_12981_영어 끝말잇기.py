from collections import deque

def solution(n, words):

    words=deque(words)
    cnt=0
    check= words[0][0] # 처음 시작은 pass 하기 위해
    call=[] # 부른 단어 저장하는 리스트

    while words:
        cnt+=1 # 전원 한 바퀴 돌때마다 cnt+1
        
        for i in range(1,n+1): # 인원수만큼 for 문 돌리기
            if not words: return [0,0] # 더 이상 큐에서 꺼낼 단어가 없을 경우 [0,0] return

            data=words.popleft()

            # call 리스트 안에 data와 같은 단어가 있거나, 끝말잇기가 틀린 경우 return
            if data[0] != check or data in call: return [i,cnt] 
            call.append(data)

            check= data[-1]

    return [0,0]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,   ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))