from itertools import product

def solution(user_id, banned_id):
    answer = []
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

        dataset[checkIdx]=data

    check=dataset.values()
  
    all_cases=list(product(*check))
   
    for case in all_cases:
        if len(set(case))==len(case):
            if set(case) not in answer:
                answer.append(set(case))

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]),2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]),2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]),3)