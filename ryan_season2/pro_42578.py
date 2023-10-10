"""
의상

[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3
"""
from collections import defaultdict


def solution(clothes):
    clothes_dict = defaultdict(list)

    for item_, class_ in clothes:
        clothes_dict[class_].append(item_)

    answer = 1
    for class_, item_list in clothes_dict.items():
        answer *= len(item_list) + 1

    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
