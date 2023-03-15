#%%
from itertools import combinations
def solution(relation):
    answer = []
    row = len(relation)
    col = len(relation[0])
    
    a = []
    
    for i in range(1,col+1):
        a.extend(list(combinations(range(col), i)))

    for i in a:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        
        if(len(set(tmp)) == row):#유일성 검사
            put = True
            
            for j in answer:#최소성
                if set(j).issubset(set(i)):
                    put = False
                    break
            
            if put == True:
                answer.append(i)
    
    return len(answer)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])


# %%
