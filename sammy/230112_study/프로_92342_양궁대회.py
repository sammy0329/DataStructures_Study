# 도전중..

def solution(n, info):
    answer = []
    win= []
    
    
    for i in range(11):
        win.append(info[i]+1)
    

    return answer

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]


# 10 9 8 7 6 5 4 3 2 1
#  3 2 2 2 1 1 1 1 1 1
 
# 10 + 9 =19 -> 15
# 9 + 8 + 6 = 23 -> 17 
# 9 + 6 + 5 + 4 = 24 -> 25
# 6 + 5 + 4 + 3 + 2 = die
# ..
