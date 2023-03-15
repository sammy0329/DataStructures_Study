def solution(brown, yellow):
    answer = []
    n,m = 3,3

    while 1:
        if(brown==((n*2 + m*2)-4) and (n*m-((n*2 + m*2)-4))==yellow):
            break
        n += 1 
        if(n+m>2502):
            m += 1
            n = 0
    answer = [n,m]
    return answer

brown = 10
yellow = 2

print(solution(brown,yellow))

