def solution(participant, completion):
    answer = ''
    parti={}
    for check in participant:
        if check not in parti:
            parti[check]=1
        else:
            parti[check]+=1
    
    for check in completion:
        if check in parti:
            parti[check]-=1
    
    for key,value in parti.items():
        if value>=1:
            answer+=key
            
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))