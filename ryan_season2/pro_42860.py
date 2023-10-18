"""
조이스틱

name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.

name	return
"JEROEN"	56
"JAN"	23
"""


def dfs(name, now, cursor=0, cnt=0, answer=[]):
    next_step = []
    for idx in range(len(name)):
        next_right = (cursor + idx) % len(name)
        if name[next_right] != now[next_right]:
            next_step.append((next_right, idx))
            break

    for idx in range(len(name)):
        next_left = (cursor - idx) % len(name)
        if name[next_left] != now[next_left]:
            next_step.append((next_left, idx))
            break

    if not next_step:
        answer.append(cnt)
        return answer

    for next_idx, mod in set(next_step):
        diff = abs(ord(name[next_idx]) - ord(now[next_idx]))
        cnt_ = cnt + min(diff, 26 - diff) + mod

        temp = now[next_idx]
        now[next_idx] = name[next_idx]

        answer = dfs(name, now, next_idx, cnt_)

        now[next_idx] = temp

    return answer


def solution(name):
    now = ['A' for _ in range(len(name))]
    answer = dfs(name, now)

    return min(answer)


print(solution("JEROEN"))
print(solution("JAN"))
