def solution(info, query):
    answer = []
    data=[]
    
    # info split 후, 리스트에 저장
    for i in range(len(info)):
        data.append(list(info[i].split()))
    
    for q in query:
        query_split=q.split(' and ')
        food,score=query_split.pop().split()
        query_split.append(food)
        
        cnt=0
        for check in data:
            if int(check[-1])<int(score): continue
            
            for qu in query_split:
                if qu != '-' and qu not in check:
                    break
            else:
                cnt+=1
                    
        answer.append(cnt)
        
    return answer

print(solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]),	[1, 1, 1, 1, 2, 4])