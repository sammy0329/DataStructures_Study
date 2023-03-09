def solution(s):
    answer = []

    s_list=[]
    newList=set()
    checkInt=''

    for idx,check in enumerate(s):
        if check !='{' and check!='}' and check != ',':
            checkInt+=check
            
        elif check == ',':
            if checkInt:
                newList.add(int(checkInt))
            # 비워주기
            checkInt=''

        elif check == '}' and idx!=len(s)-1:
            if checkInt:
                newList.add(int(checkInt))
            # 비워주기
            checkInt=''

            s_list.append(newList)
            newList=set()

    s_list.sort(key= lambda x: len(x))
    
    
    before=set()

    while s_list:
        popdata=s_list.pop(0)
        answer.append(list(popdata - before)[0])
        before=popdata
        

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"),[2, 1, 3, 4])
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"),[2, 1, 3, 4])
print(solution("{{20,111},{111}}"),	[111, 20])
