# eval 함수 활용하면 문자열에 해당하는 값 리스트로도 바꿔주기도함 !! 
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
        answer.append((popdata - before).pop())
        before=popdata
        

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"),[2, 1, 3, 4])
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"),[2, 1, 3, 4])
print(solution("{{20,111},{111}}"),	[111, 20])
