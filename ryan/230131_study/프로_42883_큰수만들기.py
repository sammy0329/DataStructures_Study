def solution(number, k):
    p = 0
    for _ in range(k):
        for idx in range(max(p-1, 0), len(number) - 1):  # range( len(number-1))
            if number[idx] < number[idx + 1]:
                number = number[:idx] + number[idx + 1:]
                p = idx
                break
        else:
            number = number[:-1]

    return number
