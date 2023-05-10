def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    stack = []
    check_O = [i for i in range(n)]
    current_idx=k
    
    for command in cmd:
        action, cnt,change_idx = '',0,0

        if len(command)!=1:
            action, cnt = command.split()
            cnt=int(cnt)
        else:
            action=command

        if action == 'U':
            if check_O and check_O.index(current_idx)-cnt>=0:
                current_idx=check_O[check_O.index(current_idx)-cnt]
            else:
                current_idx=check_O[0]
        
        elif action == 'D':
            if check_O and check_O.index(current_idx)+cnt<len(check_O):
                current_idx=check_O[check_O.index(current_idx)+cnt]
            else:
                current_idx=check_O[-1]
        
        elif action == 'C':
            stack.append(current_idx)
            
            if check_O and max(check_O)>current_idx:
                change_idx=check_O[check_O.index(current_idx)+1]
            elif check_O and max(check_O)<=current_idx:
                change_idx=check_O[check_O.index(current_idx)-1]
            
            answer[current_idx]='X'
            check_O.remove(current_idx)
            current_idx=change_idx
        
        else:
            answer[stack.pop()]='O'
            check_O.append(current_idx)
            check_O.sort()
        # print(check_O,current_idx,action)

    return "".join(answer)

print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]),"OOOOXOOO")
print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]),"OOXOXOOO")