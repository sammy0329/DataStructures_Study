def solution(s):
    num_stack = 0
    for each in s:
        if each == '(':
            num_stack += 1

        elif each == ')':
            if num_stack > 0:
                num_stack -= 1

            else:
                return False

    else:
        if num_stack != 0:
            return False

    return True


if __name__ == '__main__':
    string_input = '(()('

    if solution(string_input):
        print('true')
    else:
        print('false')
