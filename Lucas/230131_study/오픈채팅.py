#%%
def solution(record):
    answer = []
    user = {}
    result = []
    for i in record:
        if(len(i.split(" ")) == 2):
            move,uid = i.split(" ")
            name = 0
        else:
            move,uid,name = i.split(" ")
        
        if(move == "Enter" or move == "Change"):
            user[uid] = name
            
        if(move == "Change"):
             continue
        else:
            result.append(move+" "+uid)
    for i in result:
        move,uid = i.split(" ")
        if(move == "Enter"):
            answer.append((user[uid]+"님이 들어왔습니다."))
        else:
            answer.append((user[uid]+"님이 나갔습니다."))
    return answer
#%%
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

