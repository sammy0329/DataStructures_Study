def solution(clothes):
    clothes_dict = {}

    for _, kind in clothes:
        if clothes_dict.get(kind) is None:
            clothes_dict[kind] = 1
        else:
            clothes_dict[kind] += 1

    answer = 1

    for _, v in clothes_dict.items():
        answer *= (v+1)

    return answer-1


if __name__ == '__main__':
    # inp = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    inp = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(inp))

