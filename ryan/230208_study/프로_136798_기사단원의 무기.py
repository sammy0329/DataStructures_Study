def scouter(num: int) -> int:
    power = 0

    for share in range(1, int(num ** 0.5) + 1):
        if share ** 2 == num:
            power += 1
        elif num % share == 0:
            power += 2

    return power


def solution(number, limit, power):
    sumResource = 0
    for numKnight in range(1, number + 1):
        estimate = scouter(numKnight)

        if estimate <= limit:
            sumResource += estimate
        else:
            sumResource += power

    return sumResource
