from itertools import combinations


def find_new(orders, amount):
    target = {}

    for each in orders:
        if len(orders) < amount: continue

        each = sorted(each)
        for comb in combinations(each, amount):
            if target.get(comb) is None: target[comb] = 1
            else: target[comb] += 1

    max_freq = 2
    max_menu = []
    for menu, freq in target.items():
        result = ''
        for each in menu: result += each

        if freq == max_freq: max_menu.append(result)
        elif freq > max_freq:
            max_menu = [result]
            max_freq = freq

    return max_menu


def solution(orders, course):
    result = []
    for each in course:
        menu = find_new(orders, each)

        result += menu

    return sorted(result)