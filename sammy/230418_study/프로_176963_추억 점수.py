def solution(name, yearning, photo):
    answer = []
    score_dict=dict()

    for idx,n in enumerate(name):
        score_dict[n]=yearning[idx]
    
    for li in photo:
        cnt=0
        for check in li:
            if check not in score_dict:
                continue
            else:
                cnt+=score_dict[check]

        answer.append(cnt)
        
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]),	[19, 15, 6])
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]),	[67, 0, 55])
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"], ["kein", "deny", "may"], ["kon", "coni"]]),[5, 15, 0])