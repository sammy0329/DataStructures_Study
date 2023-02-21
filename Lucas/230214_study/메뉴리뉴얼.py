from itertools import combinations

def solution(orders, course):
    answer = []
    dic_list = [{}for i in range(max(course)+1)] 
    for i in orders:
        i = sorted(i)
        
        for j in course:
            a = list(combinations(i,j))
            
            for k in a:
                qe = ""
                for q in k:
                    qe += q
                if(qe not in dic_list[j]):
                    dic_list[j][qe] = 1
                else:
                    qe = ""
                    for q in k:
                        qe += q
                    dic_list[j][qe] += 1

    for i in course:
        if(dic_list[i]=={}):
            continue
        max(dic_list[i],key=dic_list[i].get)
        answer += [k for k,v in dic_list[i].items() if max(dic_list[i].values()) == v and max(dic_list[i].values()) >1]
    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
# %%
