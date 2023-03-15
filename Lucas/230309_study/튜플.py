#%%
def solution(s):
    answer = []
    #문자열로 제공된 값을 리스트에 담는다.
    s = s.replace("{"," ")
    s = s.replace("}"," ")
    s = s.split(" ")
    set_list = []
    print(s)

    for i in s:
        if i == "" or i == ",":
            continue
        else:
            tmp = []
            b = i.split(",")
            for j in b:
                tmp.append(int(j))
        
            set_list.append(tmp)
            
    set_list = sorted(set_list,key = len)
    
    for i in range(len(set_list)):
        if(i == 0):
            answer.append(set_list[i][0])
            continue
    
        answer.append(list(set(set_list[i])-set(set_list[i-1]))[0])
        
        
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# %%
a= [1,2,2,3]
set(a)
# %%
