def convert3(n, accumulate=''):
    a, b = divmod(n, 3)
    value = 2 ** b

    accumulate += str(value)

    if a == 0:
        return accumulate[::-1]

    else:
        return convert3(a, accumulate)


def solution(n):
    stage = 1  # 자릿수
    present = 3 ** stage

    while True:
        if n <= present:
            order = n - (present - 3 ** stage)
            break

        else:
            stage += 1
            present += 3 ** stage

    result = convert3(order-1)
    result = '1'*(stage-len(result)) + result

    return result
