import pandas as pd
import numpy as np

def solution(info, query):
    answer = []
    data = []
    for i in info:
        cond = list(i.split(" "))
        cond[4] = int(cond[4])
        data.append(cond)
        
    df = pd.DataFrame(data,columns = ['lang',"job","career","food","point"])
    for i in query:
        cond = list(i.split(" "))
        conds = []
        for j in range(len(cond)):
            if(cond[j] == 'and'):
                continue
            if(cond[j] == "-"):
                continue
                
            if(j == 0):
                conds.append((df["lang"] == cond[j]))
            elif(j == 2):
                conds.append((df["job"] == cond[j]))
            elif(j == 4):
                conds.append((df["career"] == cond[j]))
            elif(j == 6):
                conds.append((df["food"] == cond[j]))
            elif(j == 7):
                conds.append((df["point"] >= int(cond[j])))
        a = df
        for j in conds:
            a = a.loc[j]
        answer.append(len(a))
    return answer



solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
