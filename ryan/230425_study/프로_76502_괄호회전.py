def solution(s):
    answer = 0
    pair = {'[': ']', '{': '}', '(': ')'}
    for idx in range(len(s)):
        now_s = s[idx:] + s[:idx]
        stack = []

        for each in now_s:
            if stack and stack[-1] in pair.keys() and pair[stack[-1]] == each:
                stack.pop()
                continue

            stack.append(each)

        if not stack: answer += 1

    return answer


s = "[](){}"  # 3
print(solution(s))

s = "}]()[{"  # 2
print(solution(s))

s = "[)(]"  # 0
print(solution(s))

s = "}}}"  # 0
print(solution(s))
