from typing import List


def solution(skill: str, skill_trees: List[str]) -> int:

    count = 0

    for tree in skill_trees:
        order = [-1]

        for s in skill:
            idx = tree.find(s)
            if idx == -1:
                order.append(30)
                continue

            if max(order) > idx:
                break

            order.append(idx)

        else:
            count += 1

    return count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2
