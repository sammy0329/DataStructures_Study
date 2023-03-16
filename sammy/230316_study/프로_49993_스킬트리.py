def solution(skill, skill_trees):
    answer = 0
    # skill=list(skill)
    # skill_trees=[list(skill_tree) for skill_tree in skill_trees]

    for skill_tree in skill_trees:
        before=-1
        check_list=[]
        for idx,s in enumerate(skill):
            if s in skill_tree:
                check=skill_tree.index(s)
                if check < before: break
                before=check
                check_list.append(s)

        else:
            for i in range(len(check_list)):
                if check_list[i]!=skill[i]: break
            else:
                
                answer+=1

    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]), 2)
