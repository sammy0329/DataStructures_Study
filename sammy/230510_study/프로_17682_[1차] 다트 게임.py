def solution(dartResult):
    n = ''
    scores = []
    for check in dartResult:
        if check.isdecimal():
            n += check

        elif check == 'S':
            n = int(n)
            scores.append(n)
            n = ''

        elif check == 'D':
            n = int(n)**2
            scores.append(n)
            n = ''

        elif check == 'T':
            n = int(n)**3
            scores.append(n)
            n = ''

        elif check == '*':
            if len(scores) > 1:
                scores[-2] = scores[-2] * 2
                scores[-1] = scores[-1] * 2
            else:
                scores[-1] = scores[-1] * 2
                
        elif check == '#':
            scores[-1] = scores[-1] * -1
        
    return sum(scores)

print(solution("1S2D*3T"),37)
print(solution("1D2S0T"),3)
print(solution("1S*2T*3S"),23)
print(solution(	"1D2S#10S"),9)
