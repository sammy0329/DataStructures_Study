def solution(s):
    s = s.replace('{', '[')
    s = s.replace('}', ']')

    s: list = eval(s)

    s = [set(each) for each in s]

    s.sort(key=lambda x: len(x))

    spend = []
    for each_set in s:
        each_set: set
        now = each_set.difference(set(spend)).pop()

        spend.append(now)

    return spend


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
