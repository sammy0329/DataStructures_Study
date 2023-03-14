from collections import defaultdict,Counter

def solution(topping):
    result = 0
    young=defaultdict(int)

    older=Counter(topping)
    
    for i in range(len(topping)):
        young[topping[i]]+=1
        older[topping[i]]-=1

        if older[topping[i]]==0: del older[topping[i]]
        print(older,young)
        if len(older) == len(young): result+=1
    return result

print(solution([1, 2, 1, 3, 1, 4, 1, 2]),2)
print(solution([1, 2, 3, 1, 4]),0)