"""
올바른 괄호

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
"""


def solution(s):
    stack = []

    for each in s:
        if each == '(':
            stack.append(each)

        elif each == ')' and stack:
            stack.pop()

        else:
            return False

    if stack:
        return False

    else:
        return True



print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
