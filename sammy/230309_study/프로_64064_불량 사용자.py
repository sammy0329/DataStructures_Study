from collections import defaultdict

def solution(user_id, banned_id):
    answer = 1
    dataset=dict()

    for checkIdx,checkId in enumerate(banned_id):
        data=set()

        for userIdx,userId in enumerate(user_id):
            if len(checkId)!=len(userId): continue

            for i in range(len(checkId)):
                if checkId[i] != userId[i] and checkId[i]!='*':
                    break
            else:
                data.add(userId)

        dataset[checkId]=[len(data),data]

    check=dataset.values()

    for idx,val in enumerate(banned_id):
        max_idx=idx

        for i in range(idx+1,len(banned_id)):
            if len(dataset[val]) == len(dataset[val].intersection(dataset[banned_id[i]])): continue

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]),2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]),2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]),3)