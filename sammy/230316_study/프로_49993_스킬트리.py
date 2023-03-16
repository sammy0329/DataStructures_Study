def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        before_idx=-1 # 이전 인덱스 저장 변수
        check_list=[]

        for sk in skill:
            # skill_tree에 해당 스킬이 있다면 인덱스 뽑아서 이전 인덱스와 비교 후 이전 인덱스가 크면 순서 잘못됐기 때문에 break
            # 이전 인덱스보다 크면 before_idx 최신화 후 chek_list에 해당 스킬 append
            if sk in skill_tree: 
                check=skill_tree.index(sk)
                if check < before_idx: break
                before_idx=check
                check_list.append(sk)

        else: # break가 안걸렸다면 check_list와 skill을 앞에서 부터 하나씩 비교하기
            for i in range(len(check_list)):
                if check_list[i]!=skill[i]: break
            else:
                
                answer+=1

    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]), 2)
